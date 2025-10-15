from django.apps import apps

from django.shortcuts import get_object_or_404
from weblog.models import Interface_user, Page


def global_pages(request):
    """Global context processor for navigation pages"""
    try:
        # Django model'ini dinamik olarak al
        # Page = apps.get_model('weblog', 'Page')
        pages = Page.objects.filter(is_active=True)
        return dict(pages=pages)
    except Exception:
        # Model henüz yüklenmemişse boş liste döndür
        return dict(pages=[])


def g_online_user(request):
    online_user = get_object_or_404(Interface_user,
                                    is_online=True,
                                    is_active=True)
    return dict(online_user=online_user, )
