from django.shortcuts import render
from random import randint

# Create your views here.

def home (request):
    return render(request,"page/dynmc.html",{"platform":f"Django_render/dict ile gelen dinamik bilgi.","platform2":f"Dict ile gelen 2. dinamik bilgi : {randint(1,100)}"})
