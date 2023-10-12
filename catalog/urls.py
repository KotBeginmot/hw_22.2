from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, ContactsCreateView, ProductsListView, CategoryProductsListView, ProductCreateView, \
    ProductUpdateView, CategoryUpdateView, CategoryCreateView, CategoryDeleteView, ProductDeleteView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('category_product/<int:pk>/', CategoryProductsListView.as_view(), name='category_product'),
    path('', home, name='home'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete')

]
