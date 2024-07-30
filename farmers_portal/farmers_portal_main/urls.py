from django.urls import path
from .views import BrandListCreateView, BrandDetailView, ProductListCreateView, ProductDetailView

urlpatterns = [
    path('brands/', BrandListCreateView.as_view(), name='brand-list-create'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
