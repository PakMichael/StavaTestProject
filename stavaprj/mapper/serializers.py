from rest_framework import serializers
import re
import json


def coordinate(value):
    match = re.match('^(\-?([0-8]?[0-9](\.\d+)?|90(.[0]+)?)\s?[,]\s?)+(\-?([1]?[0-7]?[0-9](\.\d+)?|180((.[0]+)?)))$',
                     value)
    if match is None:
        raise serializers.ValidationError("Error: {0} is not a valid point".format(value))


class DistanceSerializer(serializers.Serializer):
    distance = serializers.JSONField()

    def validate(self, data):
        validated_data = []

        data_json = None

        try:
            data_json = json.loads(data['distance'])
        except Exception:
            raise serializers.ValidationError("Error: {0} is not a valid json".format(data['distance']))

        for line in data_json[:50]:
            for point in line:
                coordinate(point)
            try:
                validated_data += [(line[0], line[1])]
            except Exception:
                raise serializers.ValidationError("Error: {0} one out of two points is given".format(line))
        return validated_data


class RequestIDSerializer(serializers.Serializer):
    REQUEST_ID = serializers.CharField()

    def validate(self, data):
        return data['REQUEST_ID']
