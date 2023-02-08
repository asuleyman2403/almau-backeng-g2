from django.urls import path
from online_shop import views

urlpatterns = [
    path('categories', views.handle_categories),
    path('categories/<int:pk>', views.handle_category),
    path('categories/<int:pk>/products', views.handle_category_products),
    path('products/<int:pk>', views.handle_product)
]




