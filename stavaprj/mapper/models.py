from django.db import models


# Create your models here.

class Mapper(models.Model):
    request_id = models.CharField(max_length=128, unique=True)
    start_req_time = models.DateTimeField(null=True)
    end_req_time = models.DateTimeField(null=True)
