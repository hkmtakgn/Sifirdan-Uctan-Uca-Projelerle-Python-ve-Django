from todo.models import Todo,Category


def global_context (request):
    return dict (
        global_categories=Category.objects.filter(is_active=True),
    )

