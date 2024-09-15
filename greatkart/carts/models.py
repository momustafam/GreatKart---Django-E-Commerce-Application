from django.db import models
from store.models import Product

# Create your models here.

class Cart(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id

class CartItem(models.Model):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Processing'),
        (3, 'Shipped'),
        (4, 'Delivered'),
        (5, 'Canceled'),
    )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    def __str__(self):
        return self.product.name