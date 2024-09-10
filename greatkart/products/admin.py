from django.utils.text import slugify
from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'slug']
    
    def save_model(self, request, obj, form, change):
        """
        If the `name` field was changed, update the slug field with
        its slugified version.
        """    
        if 'name' in form.changed_data:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)
        
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'slug', 'category', 'price', 'stock_quantity', 'created_date', 'modified_date']
    
    def save_model(self, request, obj, form, change):
        """
        If the `name` field was changed, update the slug field with
        its slugified version.
        """
        if 'name' in form.changed_data:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)