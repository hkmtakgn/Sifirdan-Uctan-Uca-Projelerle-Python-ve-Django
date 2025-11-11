from fotoblog.models import Page, PageLogo


def nav_fb_pages(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            fb_pages = Page.objects.filter(is_active=True)
        elif request.user.is_active:
            fb_pages = Page.objects.filter(is_active=True).exclude(
                slug="add-page")
        else:
            fb_pages = Page.objects.filter(
                slug__in=["home", "contact", "vision", "favorites"],
                is_active=True).order_by("id")

    else:
        fb_pages = Page.objects.filter(slug__in=["home", "contact", "vision"],
                                    is_active=True).order_by("id")
    return dict(g_fb_pages=fb_pages, )


def global_logo(request):
    page_logo = PageLogo.objects.all().first()
    return dict(page_logo=page_logo, )
