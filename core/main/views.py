from django.shortcuts import render
from .models import Category, Product
# Create your views here.

def index(request):
    category_list = Category.objects.all()
    full_products = Product.objects.all()
    return render(request, 'index.html', context={
        'category_list':category_list,
        'full_products':full_products
    })

def prods(request, id):
    prod_list = Category.objects.filter(pk=id)
    category_list = Category.objects.all()
    return render(request, 'prods.html', context={
        'prod_list':prod_list,
        'category_list':category_list,

    })

def prods_detail(request, id):
    one_prod = Product.objects.get(pk=id)
    return render(request, 'prods_detail.html', context={
        'one_prod':one_prod
    })

