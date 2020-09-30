from rest_framework import serializers
from .models import District, SeaTurtleCount


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class SeaTurtleCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeaTurtleCount
        fields = '__all__'
        depth = 1


class CountPredictionDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()


class CountPredictionSerializer(serializers.Serializer):
    district = DistrictSerializer()
    real = CountPredictionDataSerializer(many=True)
    predicted = CountPredictionDataSerializer(many=True)
