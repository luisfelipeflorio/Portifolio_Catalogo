from django.contrib import admin
from .models import Category, Product

admin.site.site_header = 'Administração - Confeitaria Artesanal'
admin.site.site_title = 'Confeitaria Artesanal'
admin.site.index_title = 'Gerenciamento do Catálogo'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'price',
        'is_available',
        'is_featured',
        'created_at'
    ]
    list_filter = ['category', 'is_available', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_editable = ['is_available', 'is_featured']
