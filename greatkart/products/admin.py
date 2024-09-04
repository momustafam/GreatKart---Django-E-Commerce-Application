from django.contrib import admin
from .models import Category

# Register your models here.
models = [Category]

for model in models:
    admin.site.register(model)