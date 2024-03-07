
from django.urls import path

from main.views import catalog

urlpatterns = [
    path('', catalog)
]