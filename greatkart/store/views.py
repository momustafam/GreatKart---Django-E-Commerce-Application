from django.views.generic import TemplateView
from .models import Product, Category

class StoreView(TemplateView):
    template_name = 'store.html'
    
    from django.views.generic import TemplateView
from .models import Product, Category

class StoreView(TemplateView):
    template_name = 'store.html'
    
    def get_context_data(self, **kwargs):
        """
        Returns a dictionary representing the template context.
        
        The context must contain the following:
        
        - 'products': a QuerySet of all products in the store
        - 'categories': a QuerySet of all categories of products in the store
        """
        context = super().get_context_data(**kwargs)
        category_slug = kwargs.get('category_slug')
        
        if category_slug:
            context['products'] = Product.objects.all().filter(is_available=True, category__slug=category_slug)
            context['products_count'] = len(context['products'])
        else:
            context['products'] = Product.objects.all().filter(is_available=True)
            context['products_count'] = Product.objects.count()

        context['categories'] = Category.objects.all()

        # Return the context to be passed to the template
        return context
