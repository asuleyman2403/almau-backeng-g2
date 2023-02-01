from django.urls import path
from online_shop.views import get_categories, get_products, get_category, get_product, get_category_products, \
    get_product_of_category

urlpatterns = [
    path('categories', get_categories),
    path('products', get_products),
    path('categories/<int:pk>', get_category),
    path('categories/<int:pk>/products', get_category_products),
    path('categories/<int:pk1>/products/<int:pk2>', get_product_of_category),
    path('products/<int:pk>', get_category),
]

