from django.shortcuts import render,get_object_or_404
from developers.models import Developers,Tag

# Create your views here.


def dev_views (request,id=None):
    if not id:
        title = 'Developers Home Page'
        developers = Developers.objects.all ()
        context = dict (
            page_title=title,
            developers=developers,
        )
        return render (request,'developers/developers_home.html',context)
    else:
        title = 'Developer Details Page'
        developer = get_object_or_404 (Developers,pk=id)
        context = dict (
            developer=developer,
            page_title=title,
        )
        return render (request,'developers/developer_details.html',context)

def tag_views (request,tag_slug):
    tag = get_object_or_404 (Tag,slug=tag_slug)
    tag_name = get_object_or_404 (Tag,slug=tag_slug).title.capitalize
    context = dict (
        developers=tag.developers_set.all(),
        tag_name=tag_name,
    )
    return render (request,'developers/developers_home.html',context)


