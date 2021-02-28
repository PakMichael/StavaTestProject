from rest_framework import generics, permissions
from rest_framework.response import Response
from .RouteEvaluator import RouteEvaluator


class MapperAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        evaluator = RouteEvaluator()
        print(evaluator.evaluate().text)
        return Response('Good')
