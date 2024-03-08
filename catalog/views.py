from django.shortcuts import render


def home(request):
    return render(request, 'catalog_app/home.html')


def contact(request):
    return render(request, 'catalog_app/contact.html')
