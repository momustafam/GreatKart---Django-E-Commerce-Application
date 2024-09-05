from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category)
class Category(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'slug']