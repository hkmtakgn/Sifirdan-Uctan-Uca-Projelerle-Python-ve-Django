from todo.models import Category

def global_processor (request):
    categories = Category.objects.filter(is_active=True)
    return dict (
        categories=categories,
    ) 
