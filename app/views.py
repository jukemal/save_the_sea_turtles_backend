from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as dj_filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import District
from .serializers import DistrictSerializer


class DistrictViewset(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    ordering_fields = ["name"]

    @method_decorator(cache_page(60*60*12))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
