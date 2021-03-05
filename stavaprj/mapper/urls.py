from django.urls import path
from .api import MapperAPI

urlpatterns = [
    path('api/mapper', MapperAPI.as_view())
]

