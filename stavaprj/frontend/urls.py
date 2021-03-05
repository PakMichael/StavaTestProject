from django.urls import path
from .views import landing_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', landing_page),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
