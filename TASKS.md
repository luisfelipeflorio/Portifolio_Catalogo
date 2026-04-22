### [X] Sprint 1 — Setup e Configuração Base

#### [X] Tarefa 1.1 — Inicializar projeto Django
- [X] **1.1.1** Criar o projeto Django com `django-admin startproject config .`
- [X] **1.1.2** Verificar que `manage.py runserver` sobe sem erros
- [X] **1.1.3** Configurar `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'` em `settings.py`
- [X] **1.1.4** Configurar `STATIC_URL`, `STATICFILES_DIRS`, `MEDIA_URL` e `MEDIA_ROOT` em `settings.py`
- [X] **1.1.5** Adicionar `BASE_DIR / 'static'` ao `STATICFILES_DIRS`
- [X] **1.1.6** Adicionar `BASE_DIR / 'media'` ao `MEDIA_ROOT`

#### [X] Tarefa 1.2 — Configurar URLs globais com suporte a media em desenvolvimento
- [X] **1.2.1** Abrir `config/urls.py` e adicionar `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` condicionalmente para desenvolvimento
- [X] **1.2.2** Verificar que a rota de media está funcional

#### [X] Tarefa 1.3 — Configurar TailwindCSS via CDN no template base
- [X] **1.3.1** Criar diretório `templates/` na raiz do projeto
- [X] **1.3.2** Adicionar `BASE_DIR / 'templates'` ao `DIRS` em `TEMPLATES` no `settings.py`
- [X] **1.3.3** Criar `templates/base.html` com estrutura HTML5 completa
- [X] **1.3.4** Incluir CDN do TailwindCSS no `<head>` do `base.html`
- [X] **1.3.5** Incluir CDN do Google Fonts (Playfair Display + Inter) no `<head>`
- [X] **1.3.6** Definir `<body class="bg-[#111111] text-[#F5E6C8] font-['Inter']">` no `base.html`
- [X] **1.3.7** Adicionar bloco `{% block content %}{% endblock %}` no `base.html`

---

### Sprint 2 — App Catalog: Models e Admin

#### Tarefa 2.1 — Criar a app `catalog`
- [ ] **2.1.1** Executar `python manage.py startapp catalog`
- [ ] **2.1.2** Adicionar `'catalog'` a `INSTALLED_APPS` em `settings.py`

#### Tarefa 2.2 — Criar model `Category`
- [ ] **2.2.1** Abrir `catalog/models.py` e importar `models` e `slugify`
- [ ] **2.2.2** Criar classe `Category(models.Model)` com campos:
  - `name` — `CharField(max_length=100)`
  - `slug` — `SlugField(unique=True, blank=True)`
  - `created_at` — `DateTimeField(auto_now_add=True)`
  - `updated_at` — `DateTimeField(auto_now=True)`
- [ ] **2.2.3** Implementar `__str__` retornando `self.name`
- [ ] **2.2.4** Implementar `save()` sobrescrito que chama `slugify(self.name)` se `slug` estiver vazio
- [ ] **2.2.5** Adicionar `class Meta` com `verbose_name = 'Categoria'` e `verbose_name_plural = 'Categorias'`

#### Tarefa 2.3 — Criar model `Product`
- [ ] **2.3.1** Criar classe `Product(models.Model)` com campos:
  - `category` — `ForeignKey('Category', on_delete=models.PROTECT, related_name='products')`
  - `name` — `CharField(max_length=200)`
  - `slug` — `SlugField(unique=True, blank=True, max_length=220)`
  - `description` — `TextField(blank=True)`
  - `price` — `DecimalField(max_digits=8, decimal_places=2)`
  - `image` — `ImageField(upload_to='products/', blank=True, null=True)`
  - `is_available` — `BooleanField(default=True)`
  - `is_featured` — `BooleanField(default=False)`
  - `created_at` — `DateTimeField(auto_now_add=True)`
  - `updated_at` — `DateTimeField(auto_now=True)`
- [ ] **2.3.2** Implementar `__str__` retornando `self.name`
- [ ] **2.3.3** Implementar `save()` sobrescrito que gera `slug` a partir do `name` se vazio
- [ ] **2.3.4** Implementar `get_absolute_url()` retornando `reverse('catalog:product_detail', kwargs={'slug': self.slug})`
- [ ] **2.3.5** Adicionar `class Meta` com `verbose_name = 'Produto'`, `verbose_name_plural = 'Produtos'` e `ordering = ['-created_at']`

#### Tarefa 2.4 — Instalar dependência para ImageField
- [ ] **2.4.1** Executar `pip install Pillow`
- [ ] **2.4.2** Verificar que `Pillow` está instalado com `pip show Pillow`

#### Tarefa 2.5 — Criar e aplicar migrations
- [ ] **2.5.1** Executar `python manage.py makemigrations catalog`
- [ ] **2.5.2** Executar `python manage.py migrate`
- [ ] **2.5.3** Verificar que as tabelas foram criadas sem erros

#### Tarefa 2.6 — Registrar models no Django Admin
- [ ] **2.6.1** Abrir `catalog/admin.py`
- [ ] **2.6.2** Criar classe `CategoryAdmin(admin.ModelAdmin)` com:
  - `list_display = ['name', 'slug', 'created_at']`
  - `prepopulated_fields = {'slug': ('name',)}`
  - `search_fields = ['name']`
- [ ] **2.6.3** Criar classe `ProductAdmin(admin.ModelAdmin)` com:
  - `list_display = ['name', 'category', 'price', 'is_available', 'is_featured', 'created_at']`
  - `list_filter = ['category', 'is_available', 'is_featured']`
  - `prepopulated_fields = {'slug': ('name',)}`
  - `search_fields = ['name', 'description']`
  - `list_editable = ['is_available', 'is_featured']`
- [ ] **2.6.4** Registrar ambos com `admin.site.register(Category, CategoryAdmin)` e `admin.site.register(Product, ProductAdmin)`

#### Tarefa 2.7 — Criar superusuário e testar o Admin
- [ ] **2.7.1** Executar `python manage.py createsuperuser` e definir credenciais
- [ ] **2.7.2** Acessar `/admin/` e verificar que `Category` e `Product` aparecem
- [ ] **2.7.3** Cadastrar ao menos 2 categorias e 4 produtos de teste com imagens

---

### Sprint 3 — Views, URLs e Templates

#### Tarefa 3.1 — Configurar URLs da app `catalog`
- [ ] **3.1.1** Criar arquivo `catalog/urls.py`
- [ ] **3.1.2** Definir `app_name = 'catalog'`
- [ ] **3.1.3** Adicionar rota `''` apontando para `HomeView` com `name='home'`
- [ ] **3.1.4** Adicionar rota `'catalogo/'` apontando para `ProductListView` com `name='product_list'`
- [ ] **3.1.5** Adicionar rota `'catalogo/<slug:slug>/'` apontando para `ProductDetailView` com `name='product_detail'`
- [ ] **3.1.6** Incluir `catalog.urls` no `config/urls.py` com `include('catalog.urls')`

#### Tarefa 3.2 — Criar `HomeView`
- [ ] **3.2.1** Abrir `catalog/views.py` e importar `TemplateView`, `ListView`, `DetailView` do Django
- [ ] **3.2.2** Criar `HomeView(TemplateView)` com `template_name = 'catalog/home.html'`
- [ ] **3.2.3** Sobrescrever `get_context_data()` para adicionar `featured_products` (produtos com `is_featured=True` e `is_available=True`, limitado a 6)

#### Tarefa 3.3 — Criar `ProductListView`
- [ ] **3.3.1** Criar `ProductListView(ListView)` com:
  - `model = Product`
  - `template_name = 'catalog/product_list.html'`
  - `context_object_name = 'products'`
  - `paginate_by = 12`
- [ ] **3.3.2** Sobrescrever `get_queryset()` para filtrar por `is_available=True`
- [ ] **3.3.3** Adicionar filtro por `category` (parâmetro GET `?categoria=<slug>`)
- [ ] **3.3.4** Adicionar filtro por busca (parâmetro GET `?busca=<termo>`) usando `icontains` no campo `name`
- [ ] **3.3.5** Sobrescrever `get_context_data()` para adicionar `categories` (todas as categorias) e `current_category` (categoria selecionada)

#### Tarefa 3.4 — Criar `ProductDetailView`
- [ ] **3.4.1** Criar `ProductDetailView(DetailView)` com:
  - `model = Product`
  - `template_name = 'catalog/product_detail.html'`
  - `context_object_name = 'product'`
- [ ] **3.4.2** Verificar que o `slug_field` e `slug_url_kwarg` estão configurados corretamente (padrão do DetailView)

#### Tarefa 3.5 — Criar template `base.html`
- [ ] **3.5.1** Criar `templates/catalog/base.html` (ou mover para `templates/base.html` e herdar nos demais)
- [ ] **3.5.2** Incluir `<head>` com charset, viewport, título dinâmico `{% block title %}{% endblock %}`, Tailwind CDN e Google Fonts
- [ ] **3.5.3** Adicionar componente navbar conforme design system (seção 9.8)
- [ ] **3.5.4** Adicionar bloco `{% block content %}{% endblock %}`
- [ ] **3.5.5** Adicionar componente footer conforme design system (seção 9.9)

#### Tarefa 3.6 — Criar template `home.html`
- [ ] **3.6.1** Criar `templates/catalog/home.html` com `{% extends 'base.html' %}`
- [ ] **3.6.2** Implementar seção hero com gradiente, título da confeitaria e subtítulo
- [ ] **3.6.3** Adicionar botão "Ver Catálogo" com link para `{% url 'catalog:product_list' %}`
- [ ] **3.6.4** Implementar seção "Destaques" com grid de cards usando `featured_products`
- [ ] **3.6.5** Renderizar cada card de produto conforme design system (seção 9.6)
- [ ] **3.6.6** Adicionar condicional `{% if featured_products %}` para exibir seção somente quando houver destaques

#### Tarefa 3.7 — Criar template `product_list.html`
- [ ] **3.7.1** Criar `templates/catalog/product_list.html` com `{% extends 'base.html' %}`
- [ ] **3.7.2** Implementar barra de filtros: campo de busca (`?busca=`) e select de categorias (`?categoria=`)
- [ ] **3.7.3** Implementar `<form method="get">` para submissão dos filtros
- [ ] **3.7.4** Implementar grid de cards de produto usando `products`
- [ ] **3.7.5** Renderizar badge de destaque condicionalmente se `product.is_featured`
- [ ] **3.7.6** Renderizar badge de disponibilidade (disponível/indisponível) conforme `product.is_available`
- [ ] **3.7.7** Adicionar mensagem "Nenhum produto encontrado." quando `products` estiver vazio
- [ ] **3.7.8** Implementar paginação com links de próxima/anterior página usando `page_obj`

#### Tarefa 3.8 — Criar template `product_detail.html`
- [ ] **3.8.1** Criar `templates/catalog/product_detail.html` com `{% extends 'base.html' %}`
- [ ] **3.8.2** Implementar layout de duas colunas (foto | informações) em desktop, coluna única em mobile
- [ ] **3.8.3** Exibir foto do produto com fallback para placeholder se sem imagem
- [ ] **3.8.4** Exibir nome, categoria (com link para listagem filtrada), preço formatado, descrição e status de disponibilidade
- [ ] **3.8.5** Adicionar link "← Voltar ao Catálogo" para `{% url 'catalog:product_list' %}`

---

### Sprint 4 — Refinamentos de UI e Ajustes Finais

#### Tarefa 4.1 — Criar imagem placeholder para produtos sem foto
- [ ] **4.1.1** Adicionar um arquivo `static/images/placeholder.jpg` (imagem neutra)
- [ ] **4.1.2** Usar `{% if product.image %}` nos templates para exibir placeholder quando necessário
- [ ] **4.1.3** Verificar que o placeholder é exibido corretamente nos templates `product_list.html` e `product_detail.html`

#### Tarefa 4.2 — Formatar preço em Real brasileiro nos templates
- [ ] **4.2.1** Verificar se a localização está habilitada (`USE_L10N = True` em `settings.py`)
- [ ] **4.2.2** Usar o filtro `{{ product.price|floatformat:2 }}` nos templates ou criar um template tag customizado para formato brasileiro
- [ ] **4.2.3** Exibir preço no formato "R$ 00,00" em todos os cards e na página de detalhe

#### Tarefa 4.3 — Garantir responsividade em todas as páginas
- [ ] **4.3.1** Testar a `home.html` em viewport mobile (375px), tablet (768px) e desktop (1280px)
- [ ] **4.3.2** Testar a `product_list.html` em todos os viewports verificando o grid responsivo
- [ ] **4.3.3** Testar a `product_detail.html` verificando o layout de colunas em mobile
- [ ] **4.3.4** Corrigir eventuais quebras de layout identificadas nos testes

#### Tarefa 4.4 — Ajustes no Django Admin
- [ ] **4.4.1** Personalizar `admin.site.site_header` para o nome da confeitaria
- [ ] **4.4.2** Personalizar `admin.site.site_title` e `admin.site.index_title`
- [ ] **4.4.3** Verificar que o upload de imagem no Admin gera a pré-visualização corretamente

#### Tarefa 4.5 — Cadastrar produtos reais no catálogo
- [ ] **4.5.1** Cadastrar as categorias reais (ex: Entremets, Tortas)
- [ ] **4.5.2** Cadastrar os produtos com as fotos presentes em `images/`
- [ ] **4.5.3** Marcar os produtos principais como `is_featured=True`
- [ ] **4.5.4** Verificar que todos os produtos aparecem corretamente no catálogo

#### Tarefa 4.6 — Revisão final de código
- [ ] **4.6.1** Verificar que todo o código Python usa aspas simples
- [ ] **4.6.2** Verificar conformidade com PEP 8 (indentação, nomes de variáveis, comprimento de linha)
- [ ] **4.6.3** Verificar que toda a interface exibida ao usuário está em português brasileiro
- [ ] **4.6.4** Remover prints, comentários desnecessários e código morto
- [ ] **4.6.5** Verificar que não há funcionalidades além do escopo definido neste PRD

---

### Sprints Futuras (Backlog)

> Itens intencionalmente deixados para sprints posteriores conforme decisão de projeto.

- [ ] **Futuro** — Containerização com Docker e `docker-compose.yml`
- [ ] **Futuro** — Suite de testes automatizados (unitários e de integração)
- [ ] **Futuro** — Deploy em ambiente de produção (ex: Railway, Render, VPS)
- [ ] **Futuro** — Configuração de `WhiteNoise` para servir arquivos estáticos em produção
- [ ] **Futuro** — Compressão e otimização de imagens no upload

---