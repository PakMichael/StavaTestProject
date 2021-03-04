from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import DistanceSerializer, RequestIDSerializer
from .services import Mapper


class MapperAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        distance_ser = DistanceSerializer(data=request.data)
        distance_ser.is_valid(raise_exception=True)

        id_ser = RequestIDSerializer(data=request.data)
        id_ser.is_valid(raise_exception=True)

        mapper = Mapper(id_ser.validated_data)
        mapper.calculate_distance(distance_ser.validated_data)

        distance = mapper.distance
        execution_time = mapper.execution_time
        return Response({'Distance': distance, 'Execution Time': execution_time})
