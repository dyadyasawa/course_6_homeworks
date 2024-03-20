from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    context = {
        'objects_list': Product.objects.all(),
    }
    return render(request, 'catalog_app/home.html', context)


def contact(request):
    return render(request, 'catalog_app/contact.html')


def product_1(request):
    return render(request, 'catalog_app/product_1.html')