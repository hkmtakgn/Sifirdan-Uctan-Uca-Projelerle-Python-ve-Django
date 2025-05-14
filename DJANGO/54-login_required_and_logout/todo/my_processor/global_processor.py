from todo.models import Category


def global_category (request):
    global_categories = Category.objects.filter(is_active=True)
    return dict (
        global_categories=global_categories,
    )

