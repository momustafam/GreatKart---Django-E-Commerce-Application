from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Cart, CartItem
from store.models import Product

class CartView(TemplateView):
    template_name = 'cart.html'
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        cart = CartView.get_create_cart(self.request)

        # Fetch cart items
        cart_items = CartItem.objects.filter(cart=cart)
        
        # Calculate total price for each cart item
        bill = 0
        for item in cart_items:
            item.total_price = item.product.price * item.quantity
            bill += item.total_price
            
        context['cartItems'] = cart_items
        context['bill'] = bill

        return context
    
    @staticmethod
    def get_create_cart(request):
        # Get or create the cart from session
        """
        Get or create the cart from session.

        Args:
            session (request.session): The session to store the cart in.

        Returns:
            The session with the cart id stored in it.
        """
        cart_id = request.session.get('cartId')
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cartId'] = cart.id
        return cart

class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        """
        Handle add a product to cart request.

        Args:
            request (HttpRequest): The request containing the product id to add to the cart.

        Returns:
            HttpResponse: A redirect to the store homepage.
        """
        
        product_id = self.kwargs.get('product_id')
        
        # Get or create the cart from session
        cart = CartView.get_create_cart(request)
        
        # Handle add a product to cart request
        product = Product.objects.get(id=product_id)
        
        # Get or create CartItem
        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
        except:
            cart_item = CartItem.objects.create(cart=cart, product=product)
            cart_item.quantity = 1
            cart_item.save()

        return redirect(reverse('cart'))  # Redirect to store page or cart page
    
class RemoveFromCartView(View):
    def get(self, request, *args, **kwargs):
        
        cart_item_id = self.kwargs.get('cart_item_id')
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        cart_item.delete()

        return redirect(reverse('cart'))  # Redirect to store page or cart page
    
    
class DecreaseQuantityView(View):
    def get(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get('cart_item_id')
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        
        # Call the decrease_quantity method
        cart_item.decrease_quantity()
        cart_item.save()  # Save the updated quantity

        # Redirect back to the cart page
        return redirect(reverse('cart'))  # Assuming 'cart' is the name of your cart page URL

class IncreaseQuantityView(View):
    def get(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get('cart_item_id')
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        
        # Call the decrease_quantity method
        cart_item.increase_quantity()
        cart_item.save()  # Save the updated quantity

        # Redirect back to the cart page
        return redirect(reverse('cart'))  # Assuming 'cart' is the name of your cart page URL