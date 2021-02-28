from django.conf import settings
import requests


class RouteEvaluator():
    def __init__(self):
        self.endpoint = settings.GEO_ENDPOINT

    def evaluate(self):
        return requests.get(self.endpoint, auth=(settings.GEO_USERNAME, settings.GEO_PASSWORD))
