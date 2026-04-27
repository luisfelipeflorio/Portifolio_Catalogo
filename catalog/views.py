from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, Category


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.filter(
            is_available=True,
            is_featured=True
        )[:6]
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.filter(is_available=True)
        category_slug = self.request.GET.get('categoria')
        search_query = self.request.GET.get('busca')

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        category_slug = self.request.GET.get('categoria')
        if category_slug:
            context['current_category'] = Category.objects.filter(slug=category_slug).first()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(is_available=True)
