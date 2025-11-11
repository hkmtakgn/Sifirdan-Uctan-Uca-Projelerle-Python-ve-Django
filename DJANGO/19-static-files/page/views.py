from django.shortcuts import render

# Create your views here.

carousel_photos = [
    f"https://picsum.photos/id/{item}/1200/300" for item in range (1,4)
]

def home (request):
    title = "Home Page"
    context = dict (
        page_title=title,
        carousel_photos=carousel_photos,
    )
    return render (request,"page/home.html",context)

def contact (request):
    title = "Contact Page"
    context = dict (
        page_title=title,
    )
    return render (request,"page/contact.html",context)
