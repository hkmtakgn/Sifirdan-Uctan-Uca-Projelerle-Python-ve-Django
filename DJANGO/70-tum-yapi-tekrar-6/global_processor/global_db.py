from pages.models import Category


def global_db (request):
    items = Category.objects.filter (is_active=True)

    return dict (
        categories=items,
    )

