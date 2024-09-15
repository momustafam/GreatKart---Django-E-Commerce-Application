from django.db import models

# Create your models here.

class Category(models.Model):
    # String Fields
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    
    # Media Fields
    image = models.ImageField(upload_to='photos/categories/', blank=True, null=True)
    
    def __str__(self):
        """
        Return the name of the category as a string, which is used to
        represent the category in the admin interface and elsewhere.
        """
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        

class Product(models.Model):
    # String Fields
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    # Numeric Fields
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    
    # Boolean Fiedls
    is_available = models.BooleanField(default=True)
    
    # Media Fields
    image = models.ImageField(upload_to='photos/products/')
    
    # Date Fields
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    # Foreign Fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name