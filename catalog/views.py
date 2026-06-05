from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Product


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.filter(
            is_featured=True, is_available=True
        ).select_related('category')
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.filter(is_available=True).select_related('category')
        categoria = self.request.GET.get('categoria')
        q = self.request.GET.get('q')

        if categoria:
            queryset = queryset.filter(category__slug=categoria)
        if q:
            queryset = queryset.filter(name__icontains=q)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['categoria_ativa'] = self.request.GET.get('categoria', '')
        context['q'] = self.request.GET.get('q', '')
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'
