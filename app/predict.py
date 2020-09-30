from django_pandas.io import read_frame
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import datetime
from pathlib import Path
import os

RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)

n_steps_in, n_steps_out = 12, 8

CURRENT_DIR = Path(__file__).resolve(strict=True).parent

PREDICTION_MODEL_NAME = 'SeaTurtleCountPredictionModel'


def predict_counts(district, counts):
    df = read_frame(counts, fieldnames=[
                    'date', 'value'])

    df = df.sort_values(['date'])

    df = df.set_index('date')

    dataset = df

    print(dataset.tail(20))

    df = df.tail(n_steps_in)

    f_columns = ['value']

    scaler = MinMaxScaler(feature_range=(0, 1))

    dataset.loc[:, f_columns] = scaler.fit_transform(
        dataset[f_columns].to_numpy())

    scaled_data = dataset.tail(n_steps_in).values

    n_features = 1

    model = keras.models.load_model(
        os.path.join(CURRENT_DIR, PREDICTION_MODEL_NAME))

    x_input = scaled_data.reshape((1, n_steps_in, n_features))
    predicted_values = np.array(model.predict(x_input))

    predicted_values = scaler.inverse_transform(predicted_values[0])

    start_date = df.iloc[-1].name

    dates_array = [(start_date+pd.tseries.offsets.DateOffset(months=i)).date()
                   for i in range(3, predicted_values.shape[0]*3+1, 3)]

    final_output = pd.DataFrame(predicted_values)
    final_output['date'] = dates_array
    final_output.columns = ['value', 'date']

    print(df)

    print(final_output)

    real_list = []

    for index, row in df.iterrows():
        real_list.append({
            'date': index,
            'count': np.round(row['value']),
        })

    predicted_list = []

    for index, row in final_output.iterrows():
        predicted_list.append({
            'date': row['date'],
            'count': np.round(row['value']),
        })

    data = {
        'district': district,
        'real': real_list,
        'predicted': predicted_list,
    }

    return real_list, predicted_list, data
