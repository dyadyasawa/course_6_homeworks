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


def product_2(request):
    return render(request, 'catalog_app/product_2.html')


def product_3(request):
    return render(request, 'catalog_app/product_3.html')


def product_4(request):
    return render(request, 'catalog_app/product_4.html')


def product_5(request):
    return render(request, 'catalog_app/product_5.html')


def product_6(request):
    return render(request, 'catalog_app/product_6.html')
