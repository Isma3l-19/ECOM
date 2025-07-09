from django.urls import path
from . import views

# URL patterns for the frontend app
urlparterns = [
    path('products/', views.products, name='products'),
]