
from django.urls import path
from catalog.views import home, contact
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contact, name="contact")
]
