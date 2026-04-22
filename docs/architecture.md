# Arquitetura

## Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12+ |
| Framework | Django 5.x |
| Templating | Django Template Language (DTL) |
| CSS | TailwindCSS via CDN |
| Banco de dados | SQLite (padrão Django) |
| Mídia | Sistema de arquivos local (`MEDIA_ROOT`) |
| Admin | Django Admin nativo |

---

## Estrutura de Pastas

```
confeitaria_catalogo/
├── manage.py
├── config/                  # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── catalog/                 # App principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   └── templates/
│       └── catalog/
│           ├── base.html
│           ├── home.html
│           ├── product_list.html
│           └── product_detail.html
├── static/
│   └── css/
│       └── input.css
└── media/                   # Imagens enviadas via admin
```

---

## Modelos

### Category

| Campo | Tipo | Observação |
|---|---|---|
| `id` | PK | Auto |
| `name` | CharField | Nome da categoria |
| `slug` | SlugField | Gerado automaticamente a partir do `name` |
| `created_at` | DateTimeField | Auto |
| `updated_at` | DateTimeField | Auto |

### Product

| Campo | Tipo | Observação |
|---|---|---|
| `id` | PK | Auto |
| `category` | FK → Category | `PROTECT` — excluir categoria com produtos é bloqueado |
| `name` | CharField | Nome do produto |
| `slug` | SlugField | Gerado automaticamente a partir do `name`, único |
| `description` | TextField | Descrição completa |
| `price` | DecimalField | `max_digits=8, decimal_places=2` |
| `image` | ImageField | Upload via admin |
| `is_available` | BooleanField | Padrão `True` |
| `is_featured` | BooleanField | Padrão `False` — exibido na home |
| `created_at` | DateTimeField | Auto |
| `updated_at` | DateTimeField | Auto |

**Relação:** `Category` 1 → N `Product`

---

## Rotas

| URL | View | Descrição |
|---|---|---|
| `/` | `HomeView` | Home com produtos em destaque |
| `/catalogo/` | `ProductListView` | Listagem com filtro e busca |
| `/catalogo/<slug>/` | `ProductDetailView` | Detalhe do produto |
| `/admin/` | Django Admin | Gestão de produtos e categorias |

A busca e o filtro de categoria são passados via query string: `?q=nome` e `?categoria=slug`.
