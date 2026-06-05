from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalogo/', ProductListView.as_view(), name='product_list'),
    path('catalogo/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
