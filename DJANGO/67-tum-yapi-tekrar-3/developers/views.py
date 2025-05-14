from django.shortcuts import render,get_object_or_404
from developers.models import Developer,Category,Tag
from django.http import Http404

# Create your views here.


def dev_views (request,id=None,tag_slug=None):
    if request.path == '/developers/':
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
        context = dict (
            developer=developer,
            page_title=title,
        )
        return render (request,'main/developer_details.html',context)
    elif tag_slug:
        tag = get_object_or_404 (Tag,slug=tag_slug)
        title = tag.title.title
        context = dict (
            page_title=title,
            developers=tag.developer_set.all,
        )
        return render (request,'main/developers.html',context)
    else:
        return Http404
        

