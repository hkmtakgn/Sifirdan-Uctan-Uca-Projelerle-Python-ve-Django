from django.shortcuts import render

# Create your views here.

lorem_picsum = [
    f"https://picsum.photos/id/{id}/1200/300" for id in range (1,4)
]

def home (request):
    title = "Home Page"
    context = dict (
        page_title=title,
        lorem_picsum=lorem_picsum,
    )
    return render (request,"page/home.html",context)

def contact (request):
    title = "Contact Page"
    context = dict (
        page_title=title,
        lorem_picsum=lorem_picsum,
    )
    return render (request,"page/contact.html",context)

def aboutus (request):
    title = "About Us"
    context = dict (
        page_title=title,
        lorem_picsum=lorem_picsum,
    )
    return render (request,"page/aboutus.html",context)
