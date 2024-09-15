from .models import Category

def list_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}