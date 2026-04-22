# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Comandos

```bash
# Ambiente
python -m venv .venv
source .venv/Scripts/activate        # Windows (bash)
pip install django pillow

# Projeto
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Após alterações nos modelos
python manage.py makemigrations catalog
python manage.py migrate
```

O projeto reside dentro de `confeitaria_catalogo/` — todos os comandos `manage.py` são executados a partir dessa pasta.

---

## Arquitetura

Aplicação Django full-stack com uma única app (`catalog`) e configurações do projeto em `config/`.

**Fluxo de dados:** Django Admin → SQLite → Views (CBVs) → DTL Templates → Navegador

**App `catalog`** contém dois modelos (`Category`, `Product`), três views públicas e os templates correspondentes. Não há API, autenticação de usuário final, nem JavaScript customizado.

**Rotas públicas:**
- `/` — `HomeView`: produtos com `is_featured=True`
- `/catalogo/` — `ProductListView`: todos os produtos com `is_available=True`, filtráveis por `?categoria=<slug>` e `?q=<termo>`
- `/catalogo/<slug>/` — `ProductDetailView`: retorna 404 para slugs inexistentes

---

## Convenções Obrigatórias

- **Aspas simples** em todo código Python.
- **Class Based Views** (`TemplateView`, `ListView`, `DetailView`) — nunca function-based views.
- **Inglês** para código (nomes de variáveis, funções, classes, arquivos). **Português brasileiro** para todo texto exibido ao usuário.
- Slugs gerados via `slugify` a partir do campo `name`, com `unique=True`.
- `on_delete=models.PROTECT` na FK `Product → Category`.
- Signals em `catalog/signals.py`.
- Estilização exclusivamente via **TailwindCSS** (CDN no `base.html`) — sem CSS custom adicional.
- Todos os templates herdam de `catalog/base.html`. Sem lógica de negócio nos templates.
- Nenhuma funcionalidade além do escopo do PRD deve ser implementada.

---

## Referências

- `PRD.md` — requisitos funcionais, design system completo (paleta, tipografia, componentes Tailwind) e user stories
- `docs/` — arquitetura detalhada, design system e padrões de código
