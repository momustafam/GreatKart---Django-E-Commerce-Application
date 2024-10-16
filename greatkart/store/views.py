from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

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
        category_slug = self.kwargs.get('category_slug')
        
        if category_slug:
            category_obj = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.all().filter(is_available=True, category=category_obj).order_by('slug')
        else:
            products = Product.objects.all().filter(is_available=True).order_by('slug')

        
        search_keyword = self.request.GET.get('search')
        
        if search_keyword:
            products = products.filter(
                Q(name__icontains = search_keyword) | 
                Q(description__icontains = search_keyword) |
                Q(category__slug__icontains = search_keyword)
            )
        
        # Paginate the product queryset
        page = self.request.GET.get('page', 1)
        paginator = Paginator(products, 9)
        
        try:
            paginated_products = paginator.page(page)
        except PageNotAnInteger:
            paginated_products = paginator.page(1)
        except EmptyPage:
            paginated_products = paginator.page(paginator.num_pages)
             
        context['products'] = paginated_products
        context['products_count'] = len(context['products'])

        # Return the context to be passed to the template
        return context
    
    


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'