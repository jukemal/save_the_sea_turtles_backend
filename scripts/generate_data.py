import pandas as pd
import datetime
import numpy as np
from pathlib import Path
import os
import random

from app.models import District, SeaTurtleCount

CURRENT_DIR = Path(__file__).resolve(strict=True).parent

FILE_NAME = 'sea_turtle_population_data.csv'

np.random.seed(101)

districts = {
    1: {
        "name": "Colombo",
    },
    2: {
        "name": "Hambanthota",
    },
    3: {
        "name": "Hikkaduwa",
    },
}


def run(*args):
    df = pd.read_csv(os.path.join(
        CURRENT_DIR, FILE_NAME), parse_dates=['Date'])
    print(df.info())
    print(df.head())

    for i in range(len(districts)):
        dis = District(
            name=districts[i+1]['name'],
        )

        print(dis)

        dis.save()

        for index, row in df.iterrows():
            print(index)

            se = SeaTurtleCount(
                district=dis,
                date=row['Date'].to_pydatetime(),
                value=row['sea_turtle_count'],
            )

            print(se)

            se.save()
