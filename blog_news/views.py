from django.shortcuts import render
from rest_framework import viewsets
from .filters import NewsFilter

from .models import News
from .serializers import NewsSerializer


class NewsVeiwSet(viewsets.ModelViewSet):
    queryset = News.objects.all()#.order_by("-date_time")
    serializer_class = NewsSerializer
    filter_class = NewsFilter
