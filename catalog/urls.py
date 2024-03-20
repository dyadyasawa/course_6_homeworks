
from django.urls import path
from catalog.views import home, contact, product_1
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('product_1/', product_1, name="product_1")
]
