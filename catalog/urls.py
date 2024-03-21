
from django.urls import path
from catalog.views import home, contact, product_1, product_2, product_3, product_4, product_5, product_6
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('product_1/', product_1, name="product_1"),
    path('product_2/', product_2, name="product_2"),
    path('product_3/', product_3, name="product_3"),
    path('product_4/', product_4, name="product_4"),
    path('product_5/', product_5, name="product_5"),
    path('product_6/', product_6, name="product_6")
]
