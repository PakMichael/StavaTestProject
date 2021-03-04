from django.db import models
from .managers import MapperManager


class MapperModel(models.Model):
    objects = MapperManager()

    REQUEST_ID = models.CharField(max_length=128, unique=True)
    exec_start = models.DateTimeField(null=True)
    exec_end = models.DateTimeField(null=True)
