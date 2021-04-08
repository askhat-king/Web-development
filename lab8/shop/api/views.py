from django.shortcuts import render
from .models import product
from .models import category

def index(request):
    return render(request, 'api/index.html')

def prod(request):
    products = product.objects.all()
    return render(request, 'api/prod.html', {'products':products})

def cat(request):
    categories = category.objects.all()
    return render(request, 'api/cat.html', {'categories':categories})

def singleprod(request, id):
    singleprod = product.objects.order_by('id')[id-1:id]
    return render(request, 'api/singleprod.html', {'singleprod':singleprod})

def singlecat(request, id):
    singlecat = category.objects.order_by('id')[id-1:id]
    return render(request, 'api/singlecat.html', {'singlecat':singlecat})