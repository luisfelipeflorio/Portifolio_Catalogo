# Design System

Interface escura inspirada nas fotografias dos produtos: fundo carvão, chocolate quente, dourado de bandeja e creme de mousse.

---

## Paleta de Cores

| Token | Hex | Uso |
|---|---|---|
| `primary` | `#6B3A2A` | Botões primários, links ativos |
| `primary-dark` | `#4A2318` | Hover de botões primários |
| `accent` | `#C9A227` | Destaques, badges, bordas decorativas |
| `background` | `#111111` | Fundo principal |
| `surface` | `#1E1A18` | Cards, navbar, rodapé |
| `surface-light` | `#2C2420` | Hover de cards, inputs |
| `text-primary` | `#F5E6C8` | Textos principais |
| `text-secondary` | `#A89880` | Textos secundários, placeholders |
| `border` | `#3D2E24` | Bordas sutis |
| `success` | `#4A7C59` | Badge "Disponível" |
| `error` | `#CC2936` | Badge "Indisponível" |

---

## Tipografia

Fontes carregadas via Google Fonts no `base.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
```

| Uso | Fonte | Classes Tailwind |
|---|---|---|
| Títulos | Playfair Display | `font-['Playfair_Display'] font-bold tracking-wide` |
| Corpo | Inter | `font-['Inter'] font-light leading-relaxed` |

---

## Gradientes

```html
<!-- Hero -->
<div class="bg-gradient-to-br from-[#111111] via-[#1E1A18] to-[#2C1810]">

<!-- Overlay de card (aparece no hover) -->
<div class="bg-gradient-to-t from-[#111111]/60 to-transparent">

<!-- Barra de destaque (accent) -->
<div class="bg-gradient-to-r from-[#6B3A2A] to-[#C9A227]">
```

---

## Componentes

### Navbar

```html
<nav class="sticky top-0 z-50 bg-[#111111]/90 backdrop-blur-md border-b border-[#3D2E24]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
    <span class="font-['Playfair_Display'] text-xl font-bold text-[#C9A227] tracking-wide">
      Nome da Confeitaria
    </span>
    <div class="flex gap-6">
      <a href="/" class="text-[#A89880] hover:text-[#F5E6C8] transition-colors text-sm font-medium">Início</a>
      <a href="/catalogo/" class="text-[#A89880] hover:text-[#F5E6C8] transition-colors text-sm font-medium">Catálogo</a>
    </div>
  </div>
</nav>
```

### Rodapé

```html
<footer class="bg-[#1E1A18] border-t border-[#3D2E24] py-8 mt-16">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="font-['Playfair_Display'] text-[#C9A227] text-lg font-semibold">Nome da Confeitaria</p>
    <p class="mt-2 text-sm text-[#A89880]">Feito com carinho.</p>
  </div>
</footer>
```

### Card de Produto

```html
<div class="group bg-[#1E1A18] border border-[#3D2E24] rounded-xl overflow-hidden
            hover:border-[#C9A227]/40 transition-all duration-300 hover:-translate-y-1
            hover:shadow-lg hover:shadow-[#C9A227]/5">
  <div class="relative overflow-hidden aspect-square">
    <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
    <div class="absolute inset-0 bg-gradient-to-t from-[#111111]/60 to-transparent opacity-0
                group-hover:opacity-100 transition-opacity duration-300"></div>
  </div>
  <div class="p-4">
    <span class="text-xs text-[#C9A227] font-medium uppercase tracking-wider">Categoria</span>
    <h3 class="mt-1 font-['Playfair_Display'] text-lg text-[#F5E6C8] font-semibold">Nome</h3>
    <p class="mt-2 text-sm text-[#A89880] line-clamp-2">Descrição breve.</p>
    <div class="mt-4 flex items-center justify-between">
      <span class="font-['Playfair_Display'] text-xl text-[#C9A227] font-bold">R$ 00,00</span>
    </div>
  </div>
</div>
```

### Grid de Produtos

```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  <!-- cards -->
</div>
```

### Botões

```html
<!-- Primário -->
<button class="px-6 py-3 bg-[#6B3A2A] hover:bg-[#4A2318] text-[#F5E6C8] font-medium rounded-lg
               transition-all duration-200 border border-[#C9A227]/30 hover:border-[#C9A227]/60
               focus:outline-none focus:ring-2 focus:ring-[#C9A227]/50">

<!-- Outline -->
<button class="px-6 py-3 bg-transparent hover:bg-[#2C2420] text-[#C9A227] font-medium rounded-lg
               transition-all duration-200 border border-[#C9A227]/50 hover:border-[#C9A227]
               focus:outline-none focus:ring-2 focus:ring-[#C9A227]/50">
```

### Badges

```html
<!-- Destaque -->
<span class="px-3 py-1 bg-[#C9A227]/20 text-[#C9A227] text-xs font-medium rounded-full border border-[#C9A227]/40">
  Destaque
</span>

<!-- Disponível -->
<span class="px-3 py-1 bg-[#4A7C59]/20 text-[#4A7C59] text-xs font-medium rounded-full">
  Disponível
</span>

<!-- Indisponível -->
<span class="px-3 py-1 bg-[#CC2936]/20 text-[#CC2936] text-xs font-medium rounded-full">
  Indisponível
</span>
```

### Inputs

```html
<!-- Campo de busca -->
<input type="text"
       class="w-full px-4 py-3 bg-[#1E1A18] border border-[#3D2E24] rounded-lg
              text-[#F5E6C8] placeholder-[#A89880]
              focus:outline-none focus:border-[#C9A227]/60 focus:ring-1 focus:ring-[#C9A227]/30
              transition-colors duration-200"
       placeholder="Buscar produtos...">

<!-- Select de categoria -->
<select class="px-4 py-3 bg-[#1E1A18] border border-[#3D2E24] rounded-lg
               text-[#F5E6C8] cursor-pointer
               focus:outline-none focus:border-[#C9A227]/60
               transition-colors duration-200">
  <option>Todas as categorias</option>
</select>
```
