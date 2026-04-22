# GEMINI.md

Este arquivo fornece diretrizes e contexto para agentes de IA que trabalham neste repositório.

## Visão Geral do Projeto
Um catálogo digital de produtos de confeitaria desenvolvido com **Django 5.x**. O sistema permite que clientes visualizem o portfólio de produtos (entremets, tortas, bolos) com fotos, descrições e preços, enquanto o administrador gerencia o conteúdo via Django Admin.

- **Status Atual:** Em fase de planejamento e configuração inicial (documentação e assets prontos, implementação pendente).
- **Arquitetura:** Django full-stack (Monolítico), SQLite, TailwindCSS via CDN.

## Stack Técnica
- **Linguagem:** Python 3.12+
- **Framework:** Django 5.x (App principal: `catalog`)
- **Frontend:** Django Template Language (DTL) + TailwindCSS (CDN)
- **Banco de Dados:** SQLite
- **Imagens:** Pillow (armazenamento local em `media/`)

## Configuração e Execução

### Ambiente de Desenvolvimento
```bash
# 1. Criar e ativar ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 2. Instalar dependências
pip install django pillow

# 3. Inicializar banco de dados e admin
python manage.py migrate
python manage.py createsuperuser

# 4. Rodar o servidor
python manage.py runserver
```

### Comandos Úteis
```bash
# Criar migrations após alterar modelos
python manage.py makemigrations catalog
python manage.py migrate
```

## Convenções de Desenvolvimento

### Código Python
- **Padrão:** Seguir rigorosamente a **PEP 8**.
- **Strings:** Usar **aspas simples** (`'`) sempre que possível.
- **Idioma:** Código (variáveis, classes, arquivos) em **Inglês**. Interface do usuário em **Português Brasileiro**.
- **Views:** Utilizar exclusivamente **Class Based Views** (`ListView`, `DetailView`, `TemplateView`).
- **Models:** Slugs únicos gerados via `slugify`. FKs de `Product` → `Category` com `on_delete=models.PROTECT`.

### Frontend e Design
- **CSS:** Exclusivamente **TailwindCSS** via CDN no `base.html`. Sem CSS customizado adicional.
- **Tipografia:** Playfair Display (Headings) e Inter (Body) via Google Fonts.
- **Responsividade:** Layout deve ser funcional em Mobile, Tablet e Desktop.
- **Assets:** Imagens de produtos residem em `media/products/`. Usar placeholder se a imagem estiver ausente.

## Estrutura do Projeto (Alvo)
```
confeitaria_catalogo/
├── manage.py
├── config/                  # Configurações Django (settings, urls)
├── catalog/                 # App do Catálogo (models, views, signals)
│   ├── templates/catalog/   # Templates DTL
├── static/                  # Arquivos estáticos (CSS base, placeholders)
└── media/                   # Uploads de imagens (git-ignored)
```

## Referências de Documentação
- `PRD.md`: Requisitos detalhados e Design System completo.
- `TASKS.md`: Roadmap de implementação e status das tarefas.
- `CLAUDE.md`: Guia de comandos e restrições de arquitetura.
- `docs/`: Documentação técnica aprofundada.
