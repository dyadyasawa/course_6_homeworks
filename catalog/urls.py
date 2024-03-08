
from django.urls import path

from catalog.views import catalog

urlpatterns = [
    path('', catalog)
]