from pages.models import Page

def global_db (request):
    pages = Page.objects.filter (is_active=True)
    return dict (
        pages=pages,
    )
