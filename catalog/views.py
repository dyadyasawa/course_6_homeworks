from django.shortcuts import render


def catalog(request):
    #return render(request, 'catalog_app/index.html')
    return render(request, 'catalog_app/home.html')
