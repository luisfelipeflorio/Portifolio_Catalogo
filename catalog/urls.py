from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('catalogo/', views.ProductListView.as_view(), name='product_list'),
    path('catalogo/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
