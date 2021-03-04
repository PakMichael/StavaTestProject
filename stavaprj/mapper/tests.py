from django.test import TestCase
from .services import Mapper


# Create your tests here.

class MapperTest(TestCase):
    def make_mapper(self, REQUEST_ID) -> Mapper:
        return Mapper(REQUEST_ID)

    def test_calculating_distance(self):
        mapper = self.make_mapper('123')

        points = [
            ('-84.754482,18.1', '50.2,18.3')
        ]

        mapper.calculate_distance(points)

        distance = mapper.distance
        execution_time = mapper.execution_time

        assert distance is not None
        assert distance >= 0
        assert execution_time is not None
