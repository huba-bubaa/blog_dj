from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'url', 'content', 'image', 'video', 'likes', 'views', 'url_for_but', 'date_time', 'language']

