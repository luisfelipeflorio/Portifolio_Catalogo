---
name: clean-architecture
description: Resumo dos principais conceitos e requisitos arquiteturais do livro Clean Architecture de Robert C. Martin. Use quando precisar de orientacao sobre design de software, separacao de responsabilidades, principios SOLID, regras de dependencia, camadas arquiteturais ou boas praticas de estrutura de codigo.
---

# Clean Architecture: A Craftsman's Guide to Software Structure and Design
**Autor:** Robert C. Martin (Uncle Bob)

---

## 1. O que e Arquitetura de Software

Arquitetura nao e apenas a estrutura de pastas e arquivos — e o conjunto de decisoes de design que permitem que o sistema seja desenvolvido, implantado, mantido e estendido com o minimo de esforco humano.

**Objetivo central:** Minimizar o custo do ciclo de vida do software, maximizando a produtividade dos desenvolvedores.

> "A arquitetura de um sistema de software e a forma dada ao sistema por aqueles que o constroem, com o objetivo de facilitar seu desenvolvimento, implantacao, operacao e manutencao."

---

## 2. Comportamento vs. Estrutura

Todo sistema de software fornece dois valores distintos:

- **Comportamento (behavior):** O que o sistema faz — funcoes e features.
- **Estrutura (architecture):** A facilidade com que o comportamento pode ser alterado.

O maior problema e que gerentes e stakeholders focam apenas no comportamento, enquanto o verdadeiro valor de longo prazo esta na estrutura. Um sistema que funciona perfeitamente mas e impossivel de modificar tornara-se inutil.

---

## 3. Principios de Design: SOLID

### S — Single Responsibility Principle (SRP)
> "Um modulo deve ter um, e apenas um, motivo para mudar."

Cada classe/modulo deve ser responsavel por apenas um ator ou grupo de usuarios. Viola-lo gera acoplamento acidental entre funcionalidades distintas.

### O — Open/Closed Principle (OCP)
> "Um artefato de software deve ser aberto para extensao, mas fechado para modificacao."

Novas funcionalidades devem ser adicionadas sem alterar o codigo existente. Isto e alcancado atraves de abstraccoes e polimorfismo.

### L — Liskov Substitution Principle (LSP)
> "Subtipos devem ser substituiveis por seus tipos base."

Se uma interface promete um comportamento, todas as implementacoes devem honrar esse contrato sem surpresas para o usuario.

### I — Interface Segregation Principle (ISP)
> "Clientes nao devem ser forcados a depender de interfaces que nao usam."

Interfaces largas criam dependencias desnecessarias. Prefira interfaces pequenas e focadas.

### D — Dependency Inversion Principle (DIP)
> "Modulos de alto nivel nao devem depender de modulos de baixo nivel. Ambos devem depender de abstracoes."

Abstracoes nao devem depender de detalhes. Detalhes (implementacoes) devem depender de abstracoes. Este principio e o fundamento da Clean Architecture.

---

## 4. Principios de Coesao de Componentes

### REP — Reuse/Release Equivalence Principle
Os elementos de um componente devem ser reutilizaveis juntos e lancar versoes coesas.

### CCP — Common Closure Principle
Classes que mudam pelas mesmas razoes e ao mesmo tempo devem estar no mesmo componente. E o SRP aplicado a nivel de componente.

### CRP — Common Reuse Principle
Nao force usuarios de um componente a depender de coisas que nao precisam.

---

## 5. Principios de Acoplamento entre Componentes

### ADP — Acyclic Dependencies Principle
> "Nao deve haver ciclos no grafo de dependencias dos componentes."

Ciclos de dependencia tornam o build impossivel de isolar e dificultam a manutencao.

### SDP — Stable Dependencies Principle
> "Dependa na direcao da estabilidade."

Componentes volateis (que mudam frequentemente) nao devem ser dependencias de componentes estaveis.

### SAP — Stable Abstractions Principle
> "Um componente deve ser tao abstrato quanto e estavel."

Componentes estaveis devem ser compostos de interfaces e classes abstratas, permitindo extensao sem modificacao.

---

## 6. A Regra da Dependencia (Dependency Rule)

Este e o nucleo da Clean Architecture:

> **"As dependencias de codigo-fonte devem sempre apontar para dentro, na direcao das politicas de nivel mais alto."**

O sistema e organizado em camadas concentricas:

```
+----------------------------------+
|         Frameworks & Drivers     |  (camada mais externa)
|  +----------------------------+  |
|  |   Interface Adapters       |  |
|  |  +----------------------+  |  |
|  |  |  Application Rules   |  |  |
|  |  |  +----------------+  |  |  |
|  |  |  | Enterprise     |  |  |  |
|  |  |  | Business Rules |  |  |  |
|  |  |  +----------------+  |  |  |
|  |  +----------------------+  |  |
|  +----------------------------+  |
+----------------------------------+
```

**Nenhuma camada interna pode conhecer nada de uma camada externa.**

---

## 7. As Quatro Camadas

### Entities (Entidades)
- Encapsulam as regras de negocio criticas da empresa.
- Sao os objetos de mais alto nivel e mudam raramente.
- Nao dependem de frameworks, banco de dados ou UI.

### Use Cases (Casos de Uso)
- Contem a logica de negocio especifica da aplicacao.
- Orquestram o fluxo de dados de e para as Entidades.
- Nao conhecem banco de dados, UI ou frameworks externos.

### Interface Adapters (Adaptadores de Interface)
- Convertem dados do formato mais conveniente para Use Cases/Entities para o formato de frameworks externos.
- Incluem: Controllers, Presenters, Gateways, ViewModels.

### Frameworks & Drivers (Infra)
- Camada mais externa: banco de dados, web frameworks, UI, dispositivos.
- Contem apenas "glue code" que conecta o mundo externo ao nucleo.

---

## 8. Regras Cruzando Fronteiras

Quando dados cruzam fronteiras de camadas:
- **Sempre use estruturas de dados simples** (DTOs, structs).
- Nunca passe objetos de entidade ou objetos de framework atraves das fronteiras.
- O fluxo de controle cruza fronteiras, mas as dependencias de codigo-fonte nunca cruzam para dentro.

---

## 9. Arquitetura Gritante (Screaming Architecture)

> "A arquitetura de um sistema deve gritar sobre o que o sistema faz, nao sobre os frameworks que ele usa."

A estrutura de pastas deve refletir os casos de uso do negocio (ex: `Pedidos`, `Faturamento`, `Usuarios`), nao tecnologias (ex: `Rails`, `Spring`, `Django`).

---

## 10. A Fronteira com o Banco de Dados

O banco de dados e um **detalhe de implementacao**. A Clean Architecture exige que:
- As entidades de negocio nao saibam nada sobre persistencia.
- O acesso ao banco seja feito via **Interfaces de Gateway**, implementadas na camada de infraestrutura.
- O banco deve ser facilmente substituivel (SQL por NoSQL, por exemplo) sem tocar nas regras de negocio.

---

## 11. A Fronteira com a Web/UI

A web e um **mecanismo de entrega**, nao o nucleo do sistema. O sistema deve ser:
- Testavel sem a web.
- Capaz de funcionar via linha de comando, API REST ou qualquer outro driver externo.
- Independente do framework web utilizado.

---

## 12. Teste de Arquitetura

Uma boa arquitetura permite:
- **Testar regras de negocio sem a UI:** Testes unitarios rapidos nas Entities e Use Cases.
- **Testar regras de negocio sem o banco de dados:** Usando repositorios em memoria (in-memory fakes).
- **Testar regras de negocio sem frameworks externos:** Desacoplamento total.

> "Um bom sistema de software comeca com um codigo limpo. Voce nao pode construir uma boa arquitetura em cima de um codigo ruim."

---

## 13. Independencia

Uma boa arquitetura deve suportar independencia em quatro dimensoes:

| Dimensao | Descricao |
|---|---|
| **Independencia de Framework** | O sistema nao depende de features especificas de um framework. |
| **Independencia de UI** | A UI pode mudar (web para CLI para mobile) sem afetar o negocio. |
| **Independencia de Banco de Dados** | O banco pode ser trocado sem impacto nas regras de negocio. |
| **Independencia de Agentes Externos** | Regras de negocio nao conhecem o mundo externo (APIs de terceiros, etc.). |

---

## 14. Limites (Boundaries) e Plugins

A arquitetura deve tratar modulos externos como **plugins**:
- O nucleo (regras de negocio) define interfaces.
- Detalhes externos implementam essas interfaces.
- Isso cria um modelo de "plugin architecture" onde detalhes podem ser substituidos sem afetar o nucleo.

---

## 15. Humildade vs. Fanatismo Arquitetural

Robert Martin alerta: arquitetura tem custo. Nao implemente fronteiras onde nao ha necessidade real. O desafio do arquiteto e:

> "Determinar onde estao as fronteiras arquiteturais e quando torna-las totalmente concretas, parcialmente concretas ou ignoradas por enquanto."

Use o julgamento profissional para aplicar os principios de forma pragmatica, nao dogmatica.

---

## Resumo dos Requisitos Principais

1. **Separacao de responsabilidades** entre camadas de negocio e infra.
2. **Regra da dependencia:** dependencias sempre apontam para dentro.
3. **Entidades livres de frameworks**, banco e UI.
4. **Casos de Uso** como unidade central da logica de aplicacao.
5. **Interfaces como contratos** entre camadas.
6. **Testabilidade** como requisito de design, nao aftertought.
7. **Banco de dados e Web sao detalhes** — plugaveis e substituiveis.
8. **Arquitetura deve refletir o negocio**, nao a tecnologia.
9. **Componentes estaveis** devem ser abstratos; os volateis, concretos.
10. **Sem ciclos** no grafo de dependencias entre componentes.

---

*Fonte: Clean Architecture: A Craftsman's Guide to Software Structure and Design — Robert C. Martin (2017)*
