from django.shortcuts import render,get_object_or_404
from developers.models import Developer,Tag
import lorem
import random

# Create your views here.


def dev_views (request,id=None):
    if not id:
        title = 'X-Developers'
        developers = Developer.objects.filter (is_active=True)
        context = dict (
            page_title=title,
            developers=developers,
        )
        return render (request,'main/developers.html',context)
    elif id:
        title = 'Developer Details'
        developer = get_object_or_404 (Developer,pk=id)
        lorem_text = lorem.text()[:34]+'...'
        context = dict (
            page_title=title,
            developer=developer,
            lorem_text=lorem_text,
        )
        return render (request,'main/developer_details.html',context)

def tag_views (request,tag_slug):
    tag = get_object_or_404 (Tag,slug=tag_slug)
    title = tag.title.title
    context = dict (
        page_title=title,
        developers=tag.developer_set.all(),
    )
    return render (request,'main/developers.html',context)

