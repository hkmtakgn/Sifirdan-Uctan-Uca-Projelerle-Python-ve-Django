from django.shortcuts import render

# Create your views here.

FAKE_DB_PROJECTS = [
    f"https://picsum.photos/id/{id}/200/300" for id in range(1,8)
]

def home (request):
    title = "Home Page"
    context = dict (
        page_title = title,
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render (request,"page/home.html",context)

def contact (request):
    title = "Contact"
    context = dict (
        page_title = title,
    )
    return render (request,"page/contact.html",context)
