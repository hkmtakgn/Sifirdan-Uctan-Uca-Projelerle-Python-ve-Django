from django.shortcuts import render

# Create your views here.

fake_db_carousel = [
    f"https://picsum.photos/id/{id}/1200/300" for id in range (1,4)
]

def home (request):
    title = "Carousel"
    context = dict (
        page_title = title,
        fake_db_carousel = fake_db_carousel,
    )
    return render (request,"page/home.html",context)
