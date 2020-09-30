from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as dj_filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import District, SeaTurtleCount
from .serializers import DistrictSerializer, SeaTurtleCountSerializer, CountPredictionSerializer
from .filters import SeaTurtleCountFilter
from .predict import predict_counts


class DistrictViewset(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    ordering_fields = ["name"]

    @method_decorator(cache_page(60*5))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SeaTurtleCountViewset(viewsets.ReadOnlyModelViewSet):
    queryset = SeaTurtleCount.objects.all()
    serializer_class = SeaTurtleCountSerializer
    ordering_fields = ["date"]
    filter_class = SeaTurtleCountFilter

    @method_decorator(cache_page(60*5))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CountPredictionViewSet(viewsets.ViewSet):

    @method_decorator(cache_page(60*5))
    def retrieve(self, request, pk=None):
        district = get_object_or_404(District, pk=pk)

        counts = SeaTurtleCount.objects.filter(
            district__id=pk).order_by('date')

        *_, data = predict_counts(
            district, counts)

        serializer = CountPredictionSerializer(data, read_only=True)

        return Response(serializer.data)
