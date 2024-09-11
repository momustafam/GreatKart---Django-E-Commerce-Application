from django.views.generic import ListView
from store.models import Product

# Create your views here.

class LandingPageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.all().filter(is_available=True)[:12] # Slicing here limits the sql query to obtain only first 12 products.