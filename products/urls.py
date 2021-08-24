from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('add/<item_id>/', views.add_to_cart, name="add_to_cart"),
]
