# Agentes

Agentes de IA especializados no time de desenvolvimento do Catálogo de Confeitaria.

Para usar um agente no Claude Code: `claude --agent <nome>` ou invoque pelo nome em uma conversa com `@<nome>`.

---

## Índice

| Agente | Arquivo | Quando usar |
|---|---|---|
| [backend](#backend) | [backend.md](backend.md) | Models, views, URLs, admin, migrations |
| [frontend](#frontend) | [frontend.md](frontend.md) | Templates HTML, componentes TailwindCSS |
| [qa](#qa) | [qa.md](qa.md) | Testes funcionais e de design no sistema em execução |

---

## backend

**Especialidade:** Django 5.x · Python 3.12+ · SQLite

Responsável por toda a camada Python do projeto: modelos `Category` e `Product`, views baseadas em classe (`HomeView`, `ProductListView`, `ProductDetailView`), roteamento de URLs, configuração do Django Admin e migrations.

Usa o **MCP Context7** para consultar a documentação atualizada do Django antes de escrever código.

**Use quando precisar de:**
- Criar ou alterar modelos e rodar migrations
- Implementar ou corrigir views e filtros de busca/categoria
- Configurar o Django Admin com `list_display`, `list_filter` e `prepopulated_fields`
- Configurar `settings.py`, `urls.py` ou `wsgi.py`

---

## frontend

**Especialidade:** Django Template Language · TailwindCSS · Design system do projeto

Responsável por todos os arquivos em `catalog/templates/catalog/`. Conhece o design system completo: paleta de cores (`#111111`, `#C9A227`, `#F5E6C8` etc.), tipografia (Playfair Display + Inter), e todos os componentes definidos (cards, badges, inputs, navbar, rodapé).

Usa o **MCP Context7** para consultar a documentação atualizada de TailwindCSS e Django templates.

**Use quando precisar de:**
- Criar ou modificar qualquer template HTML
- Implementar componentes do design system (cards, badges, inputs, botões)
- Ajustar responsividade (mobile / tablet / desktop)
- Corrigir classes Tailwind ou estrutura de template

---

## qa

**Especialidade:** Testes funcionais e visuais via Playwright

Acessa o sistema em execução (`http://localhost:8000`) e valida se todas as funcionalidades e o design estão corretos. Cobre as três rotas públicas (`/`, `/catalogo/`, `/catalogo/<slug>/`), filtros, busca, 404, responsividade e fidelidade visual ao design system.

Usa o **MCP Playwright** para navegar, interagir com a UI e tirar screenshots.

**Use quando precisar de:**
- Verificar se uma feature implementada funciona corretamente no browser
- Validar que o design está fiel ao design system após mudanças de template
- Testar responsividade nos breakpoints mobile, tablet e desktop
- Confirmar comportamento de filtros, busca e navegação entre páginas

> **Pré-requisito:** o servidor deve estar em execução com `python manage.py runserver` antes de invocar este agente.
