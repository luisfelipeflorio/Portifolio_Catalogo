# Padrões de Código

## Python / Django

- Seguir **PEP 8** em todo o código Python.
- Usar **aspas simples** (`'`) em strings Python.
- Nomes de variáveis, funções, classes e arquivos em **inglês**.
- Todo texto exibido ao usuário em **português brasileiro**.
- Usar **Class Based Views** sempre que possível (`TemplateView`, `ListView`, `DetailView`).
- Signals, quando necessários, devem ficar em `catalog/signals.py`.
- Não implementar nenhuma funcionalidade fora do escopo definido.

## Modelos

- Todos os modelos devem ter os campos `created_at` e `updated_at` com `auto_now_add` e `auto_now` respectivamente.
- Slugs são gerados automaticamente a partir do campo `name` usando `slugify`.
- O campo `slug` deve ser `unique=True` em ambos os modelos.
- A FK de `Product` para `Category` deve usar `on_delete=models.PROTECT`.

## Templates

- Todos os templates herdam de `catalog/base.html`.
- Nenhuma lógica de negócio nos templates — apenas renderização.
- Preços formatados como `R$ 00,00` (padrão brasileiro).
- Produtos sem imagem exibem um placeholder via condicional no template.

## Admin

- Usar classes customizadas (`ModelAdmin`) para `Product` e `Category`.
- O slug deve ser pré-populado a partir do `name` no admin (`prepopulated_fields`).
- `list_display`, `list_filter` e `search_fields` configurados para facilitar a gestão.

## CSS / Frontend

- Estilização exclusivamente via **TailwindCSS** (sem CSS custom, exceto o arquivo `static/css/input.css` para configuração base).
- TailwindCSS carregado via CDN no `base.html`.
- Nenhum framework JavaScript além do que o Django fornece por padrão.
- Layout responsivo obrigatório: mobile, tablet e desktop.
