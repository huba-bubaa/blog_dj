from django_filters import rest_framework as filters
from .models import News


class NewsFilter(filters.FilterSet):
    language = filters.CharFilter(field_name="language")

    class Meta:
        model = News
        fields = ['language']
