from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active']
    list_display_links = ['email', 'username', 'first_name', 'last_name']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['last_login']
    
    # For now, not applying horizontal filters or list filters, or customizing fieldsets
    filter_horizontal = ()  # No many-to-many relationships to filter
    list_filter = ()  # No sidebar filters to display
    fieldsets = ()  # Default layout of fields, no custom grouping