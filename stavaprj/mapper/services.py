import requests
from django.conf import settings
from .models import MapperModel


def get_distance_from_remote(origin, destination) -> int:
    params = {"origin": origin, "destination": destination}
    response = requests.get(settings.GEO_ENDPOINT, auth=settings.GEO_AUTH, params=params)
    j_response = response.json()

    if 'distance' not in j_response:
        raise Exception('Failed to get distance from remote')

    return j_response['distance']


class Mapper():
    distance: int = 0

    def __init__(self, REQUEST_ID: str):
        self.REQUEST_ID = REQUEST_ID
        self.integration, self.is_new = MapperModel.objects.get_or_create(REQUEST_ID=REQUEST_ID)

    def calculate_distance(self, points):
        self.distance = 0
        MapperModel.objects.set_execution_start(self.integration)

        for origin, destination in points:
            self.distance += get_distance_from_remote(origin, destination)

            passed_seconds = MapperModel.objects.get_passed_seconds(self.integration)
            print('passed_seconds', passed_seconds)
            if passed_seconds >= 10:
                break

        MapperModel.objects.set_execution_stop(self.integration)

    @property
    def distance(self) -> float:
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def execution_time(self) -> float:
        return MapperModel.objects.get_execution_time(self.integration)
