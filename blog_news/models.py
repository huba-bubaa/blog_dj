from django.db import models
from embed_video.fields import EmbedVideoField

RUSSIAN = 'ru'
ENGLISH = "en"
TURKISH = "tr"

LANGUAGES = [
    (RUSSIAN, 'Russian'),
    (ENGLISH, 'English'),
    (TURKISH, 'Turkish')
]


class News(models.Model):
    image = models.ImageField(null=True)
    video = models.FileField(null=True)
    content = models.CharField(max_length=300)
    views = models.IntegerField(default=0)
    url_for_but = models.CharField(max_length=500, default="")
    likes = models.IntegerField(default=0)
    language = models.CharField(choices=LANGUAGES, max_length=10)
    date_time = models.DateTimeField(auto_now=True)

