from django.shortcuts import render

# Create your views here.

picSrc = "https://picsum.photos/id/313/200/300"

pic_url = dict (
    picSrc = picSrc
)

def home(request):
    return render (request,"page/home.html",pic_url)

