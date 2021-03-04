from django.db import models
from django.utils import timezone


class MapperManager(models.Manager):
    def set_execution_start(self, mapper):
        mapper.exec_start = timezone.now()
        mapper.save()

    def set_execution_stop(self, mapper):
        mapper.exec_end = timezone.now()
        mapper.save()

    def get_execution_time(self, mapper) :
        return (mapper.exec_end - mapper.exec_start)

    def get_passed_seconds(self, mapper):
        return (timezone.now() - mapper.exec_start).seconds
