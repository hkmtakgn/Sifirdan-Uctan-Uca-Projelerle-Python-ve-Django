from django.shortcuts import render

# Create your views here.

def pro_view (request):
    return render (request,"products/products.html",{})

def mini_pro_view (request):
    return render (request,"products/mini_products.html",{})

