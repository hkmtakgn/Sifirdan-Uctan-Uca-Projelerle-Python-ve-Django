from django.shortcuts import render
from developers.models import Developer,Tag
from django.shortcuts import get_object_or_404
import lorem

# Create your views here.



def dev_views (request,id=None):
    if not id:
        developers = Developer.objects.filter (is_active=True)
        context = dict (
            page_title='X-Developers',
            developers=developers,
        )
        return render (request,'main/users.html',context)
    elif id:
        id = get_object_or_404 (Developer,pk=id).pk
        lorem_ipsum = lorem.text()[:id * 100] + '...'
        developer = get_object_or_404 (Developer,pk=id)
        context = dict (
            developer=developer,
            lorem_ipsum=lorem_ipsum,
        )
        return render (request,'main/user_details.html',context)


def tag_views (request,tag_slug=None):
    tag = get_object_or_404 (Tag,slug=tag_slug)
    context = dict (
        developers=tag.developer_set.all,
        tag_title=f'{tag.title} Developers',
    )
    return render (request,'main/users.html',context)

