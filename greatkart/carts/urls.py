from django.urls import path
from . import views

urlpatterns = [
    path("", views.CartView.as_view(), name='cart'),
    path("add_cart_item/<int:product_id>", views.AddToCartView.as_view(), name='add_cart_item'),
    path("remove_cart_item/<int:cart_item_id>", views.RemoveFromCartView.as_view(), name='remove_cart_item'),
    path('increase_quantity/<int:cart_item_id>', views.IncreaseQuantityView.as_view(), name="increase_cart_item_quantity"),
    path('decrease_quantity/<int:cart_item_id>', views.DecreaseQuantityView.as_view(), name="decrease_cart_item_quantity"),
]