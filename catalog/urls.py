
from django.urls import path
from catalog.views import home, contact, product, blank
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('product/', product, name="product"),
    path('blank/', blank, name="blank")
]
