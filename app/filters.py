from django_filters import rest_framework as filters
from .models import SeaTurtleCount


class SeaTurtleCountFilter(filters.FilterSet):
    district_name = filters.CharFilter(
        field_name="district__name", lookup_expr="exact")
    district_id = filters.CharFilter(
        field_name="district__id", lookup_expr="exact")

    class Meta:
        model = SeaTurtleCount
        fields = ["district_name", "district_id"]
