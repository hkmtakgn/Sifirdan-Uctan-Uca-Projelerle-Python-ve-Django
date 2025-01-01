from todo.models import Category


def my_global_categories (request):
    return dict (
        categories=Category.objects.filter(is_active=True),
    )

