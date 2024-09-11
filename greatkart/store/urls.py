from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
    path('<slug:category_slug>', views.StoreView.as_view(), name='category_store')
]