from .models import Cart, CartItem

def cart_items_count(request):
    try:
        cart = Cart.objects.get(id=request.session['cartId'])
        items_count = CartItem.objects.filter(cart=cart).count()
    except:
        items_count = 0
    return {'cart_items_count': items_count}