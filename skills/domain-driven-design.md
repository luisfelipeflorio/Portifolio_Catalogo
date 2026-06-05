---
name: domain-driven-design
description: Resumo dos principais conceitos e requisitos do livro Implementing Domain-Driven Design de Vaughn Vernon. Use quando precisar de orientacao sobre DDD, Bounded Contexts, Aggregates, Entities, Value Objects, Domain Events, Repositories, Application Services, CQRS, Event Sourcing ou linguagem ubiqua no design de software orientado a dominio.
---

# Implementing Domain-Driven Design (IDDD)
**Autor:** Vaughn Vernon (2013)

> Este livro e o guia pratico definitivo para aplicar o Domain-Driven Design (DDD) originalmente conceituado por Eric Evans em "Domain-Driven Design: Tackling Complexity in the Heart of Software" (2003).

---

## 1. O que e Domain-Driven Design (DDD)

DDD e uma abordagem de desenvolvimento de software que coloca o **dominio de negocio** no centro do design do sistema. A ideia central e que o software deve refletir fielmente o modelo mental que especialistas de dominio (domain experts) possuem do negocio.

**Objetivos principais:**
- Alinhar software e negocio por meio de uma linguagem compartilhada.
- Gerenciar a complexidade de dominios ricos e complexos.
- Criar software que e genuinamente util para o negocio.

---

## 2. Linguagem Ubiqua (Ubiquitous Language)

A Linguagem Ubiqua e um vocabulario **rigoroso e compartilhado** entre desenvolvedores e especialistas de dominio.

**Requisitos:**
- Todo conceito de dominio deve ter um unico nome consistente em codigo, conversas, documentos e testes.
- Termos tecnicos (ex: `DAO`, `Manager`, `Helper`) devem ser evitados no nucleo do dominio.
- A linguagem deve evoluir junto com o entendimento do negocio.
- O codigo deve "falar" o dominio: `pedido.confirmar()` em vez de `pedidoService.setStatus(pedido, "CONFIRMADO")`.

> "Se a linguagem no codigo diverge da linguagem falada, o software torna-se um campo minado."

---

## 3. Bounded Context (Contexto Delimitado)

O Bounded Context e a fronteira explicita dentro da qual um modelo de dominio e definido e aplicado. Cada contexto tem sua propria Linguagem Ubiqua.

**Requisitos:**
- Cada Bounded Context deve ter um modelo de dominio independente e coeso.
- Um conceito (ex: `Cliente`) pode ter significados diferentes em contextos diferentes — isso e intencional e correto.
- Os limites devem ser explicitamente documentados no **Context Map**.
- Comunicacao entre contextos deve ser feita via interfaces bem definidas.

### Padroes de Relacionamento entre Contextos

| Padrao | Descricao |
|---|---|
| **Shared Kernel** | Dois contextos compartilham um subconjunto do modelo. |
| **Customer-Supplier** | Um contexto (upstream) produz para outro (downstream). |
| **Conformist** | O downstream adota o modelo do upstream sem negociacao. |
| **Anti-Corruption Layer (ACL)** | Camada de traducao que protege o modelo do downstream de modelos externos. |
| **Open Host Service** | Protocolo aberto para integracao com multiplos consumidores. |
| **Published Language** | Linguagem bem documentada para troca de dados entre contextos. |
| **Separate Ways** | Contextos sem integracao, cada um resolve seu problema independentemente. |

---

## 4. Blocos de Construcao Taticos (Building Blocks)

### 4.1 Entities (Entidades)

- Objetos com **identidade unica e continua** ao longo do tempo.
- A identidade persiste mesmo que os atributos mudem.
- Deve-se usar um **identificador unico** (ex: UUID) — nunca depender de IDs gerados pelo banco.
- Entidades possuem **comportamento de dominio** (metodos que expressam regras de negocio).

**Requisitos de implementacao:**
- A identidade deve ser estabelecida no momento da criacao.
- Nunca expor setters publicos; use metodos de negocio expressivos.
- Invariantes devem ser protegidas dentro da entidade.

```
// Errado: anaemico
pedido.setStatus("CONFIRMADO");

// Correto: rico em dominio
pedido.confirmar();
```

### 4.2 Value Objects (Objetos de Valor)

- Objetos sem identidade propria, definidos apenas pelos seus **atributos**.
- Sao **imutaveis**: uma vez criados, nao mudam — substituem-se por novos.
- Devem encapsular conceitos de dominio precisos (ex: `Dinheiro`, `Endereco`, `CPF`).

**Requisitos de implementacao:**
- Implementar igualdade por valor, nao por referencia.
- Nao possuir ID.
- Ser imutavel (sem setters, campos `final`/`readonly`).
- Fazer validacoes no construtor.

### 4.3 Aggregates (Agregados)

O Aggregate e o conceito tatico mais importante do DDD. E um **cluster de objetos relacionados** tratados como uma unidade para fins de mudanca de dados.

**Requisitos:**
- Cada Aggregate tem uma **Aggregate Root** (Entidade Raiz) que e o unico ponto de acesso externo.
- Nenhum objeto externo pode referenciar diretamente um objeto interno do Aggregate — apenas a raiz.
- Todo Aggregate deve proteger suas **invariantes de negocio** internamente.
- **Aggregates devem ser pequenos.** O tamanho e um sinal de design.
- Transacoes devem modificar apenas **um Aggregate por vez**.
- Consistencia entre Aggregates deve ser eventual, nao transacional.

> "Projete Aggregates pequenos. Modifique apenas um Aggregate por transacao. Use consistencia eventual entre Aggregates."

### 4.4 Domain Services (Servicos de Dominio)

- Operacoes de dominio que **nao pertencem naturalmente** a nenhuma Entidade ou Value Object.
- Devem ser **stateless** (sem estado).
- O nome deve refletir a Linguagem Ubiqua.

**Quando usar:**
- A operacao envolve multiplas entidades.
- A operacao representa um conceito de dominio importante (ex: `TransferenciaFinanceira`).
- Colocar a operacao em uma entidade violaria seu coeso.

### 4.5 Domain Events (Eventos de Dominio)

- Representam **algo que aconteceu no dominio** e que e relevante para o negocio.
- Sao imutaveis (registram o passado).
- Nomeados no passado: `PedidoConfirmado`, `PagamentoRecebido`, `UsuarioCadastrado`.

**Requisitos:**
- Devem conter toda informacao necessaria para que consumidores reajam ao evento.
- Publicados apos a transacao confirmar a mudanca de estado.
- Sao o mecanismo para consistencia eventual entre Aggregates e entre Bounded Contexts.

### 4.6 Repositories (Repositorios)

- Abstracoes para **persistencia e recuperacao de Aggregates**.
- Cada Aggregate Root deve ter exatamente um Repository.
- A interface do Repository pertence ao dominio; a implementacao pertence a infraestrutura.

**Requisitos:**
- Apenas Aggregate Roots devem ter Repositories — nunca entidades internas.
- A interface deve usar termos da Linguagem Ubiqua.
- Nunca expor metodos de consulta genericos como `findAll()` sem filtros em dominios complexos.

### 4.7 Factories (Fabricas)

- Encapsulam a logica complexa de criacao de Aggregates ou Entities.
- Usadas quando o construtor da entidade nao e suficiente para expressar o processo de criacao.
- Podem ser metodos de fabrica estaticos, classes dedicadas ou metodos na Aggregate Root.

---

## 5. Application Services (Servicos de Aplicacao)

- Orquestram casos de uso da aplicacao coordenando Aggregates, Repositories e Domain Services.
- Sao a fronteira entre a camada de dominio e o mundo externo (UI, API, mensageria).
- **Nao contem logica de negocio** — delegam para o dominio.
- Gerenciam transacoes e controle de acesso.

```
// Application Service: fino e orquestrador
class ConfirmarPedidoService {
    fun confirmar(pedidoId: PedidoId) {
        val pedido = pedidoRepository.buscarPorId(pedidoId)
        pedido.confirmar()  // logica de dominio na entidade
        pedidoRepository.salvar(pedido)
        // publica Domain Event
    }
}
```

---

## 6. Context Mapping (Mapeamento de Contextos)

O Context Map e a visualizacao das relacoes e integracoes entre todos os Bounded Contexts do sistema.

**Requisitos:**
- Todo projeto DDD deve ter um Context Map documentado.
- Deve mostrar explicitamente os padroes de relacionamento entre contextos.
- Deve ser mantido atualizado conforme o sistema evolui.
- Ajuda a identificar onde aplicar Anti-Corruption Layers.

---

## 7. Arquitetura para DDD

### Arquitetura Hexagonal (Ports and Adapters)

Recomendada como arquitetura primaria para aplicacoes DDD:

```
+----------------------------------------------+
|              Adaptadores (UI, API, DB)        |
|   +----------------------------------+        |
|   |        Application Services     |        |
|   |  +----------------------------+ |        |
|   |  |    Domain Model            | |        |
|   |  | (Entities, Aggregates,     | |        |
|   |  |  Value Objects, Events,    | |        |
|   |  |  Domain Services)          | |        |
|   |  +----------------------------+ |        |
|   +----------------------------------+        |
+----------------------------------------------+
```

- **Ports (Portas):** Interfaces definidas pelo dominio/aplicacao.
- **Adapters (Adaptadores):** Implementacoes concretas (banco de dados, REST, mensageria).
- O dominio nao depende de frameworks, banco de dados ou infraestrutura.

### Outras Arquiteturas Compativeis
- **Layered Architecture (Arquitetura em Camadas)** tradicional.
- **Event-Driven Architecture** com publicacao de Domain Events.
- **CQRS + Event Sourcing** para contextos de alta complexidade.

---

## 8. CQRS (Command Query Responsibility Segregation)

Separa as operacoes de **escrita (Commands)** das operacoes de **leitura (Queries)** em modelos distintos.

**Quando aplicar:**
- Quando o modelo de leitura e o modelo de escrita tem formas muito diferentes.
- Quando ha alta demanda de consultas que nao justificam atravessar o modelo de dominio.
- Em conjunto com Event Sourcing.

**Requisitos:**
- Commands alteram estado e retornam void (ou apenas confirmacao).
- Queries retornam dados e nao alteram estado.
- O modelo de leitura (Read Model) pode ser um banco de dados separado, otimizado para consultas.

---

## 9. Event Sourcing

Em vez de persistir o estado atual de um Aggregate, persiste-se a **sequencia de Domain Events** que levaram ao estado atual.

**Beneficios:**
- Historico completo e auditavel de todas as mudancas.
- Possibilidade de reconstruir o estado em qualquer ponto no tempo.
- Base natural para CQRS.

**Requisitos:**
- Cada mudanca de estado deve gerar um Domain Event.
- O estado do Aggregate e reconstruido replaying os eventos.
- Os eventos sao imutaveis e nunca deletados.

---

## 10. Distilacao do Dominio

Nem todas as partes do dominio tem o mesmo valor estrategico. Vernon categoriza:

| Categoria | Descricao | Investimento |
|---|---|---|
| **Core Domain** | O nucleo do negocio, vantagem competitiva. | Alto — melhor equipe, DDD completo. |
| **Supporting Subdomain** | Suporta o Core, mas nao e diferencial. | Medio — pode terceirizar ou simplificar. |
| **Generic Subdomain** | Comum a varios negocios, sem diferencial. | Baixo — usar solucoes prontas (ex: auth, pagamento). |

> "Invista seus melhores recursos no Core Domain. Nao trate tudo igualmente."

---

## 11. Big Picture Event Storming

Tecnica de modelagem colaborativa para descobrir o dominio:

- Reune desenvolvedores e especialistas de dominio em uma sessao de modelagem.
- Usa post-its de diferentes cores para mapear Domain Events, Commands, Aggregates e Bounded Contexts.
- Resultado: entendimento compartilhado do dominio e identificacao dos Bounded Contexts.

---

## 12. Integracoes entre Bounded Contexts

### Mensageria Assincrona
- Bounded Contexts se comunicam via Domain Events publicados em um barramento de mensagens.
- Garante desacoplamento e consistencia eventual.

### REST / RPC
- Quando necessario, usar Anti-Corruption Layer para traduzir modelos externos.
- Nunca deixar um modelo externo "vazar" para dentro do seu Bounded Context.

---

## Resumo dos Requisitos Principais

1. **Linguagem Ubiqua:** todo conceito de dominio tem um nome unico, consistente no codigo e nas conversas.
2. **Bounded Contexts** claramente definidos com limites explicitamente documentados no Context Map.
3. **Aggregates pequenos** — protegem invariantes e sao a unidade de transacao.
4. **Apenas um Aggregate modificado por transacao;** consistencia eventual entre Aggregates.
5. **Aggregate Roots** como unico ponto de acesso externo ao Aggregate.
6. **Value Objects imutaveis** para conceitos sem identidade propria.
7. **Domain Events** nomeados no passado para capturar fatos de negocio.
8. **Repositories** apenas para Aggregate Roots, com interface no dominio.
9. **Application Services** finos, sem logica de negocio, apenas orquestracao.
10. **Anti-Corruption Layer** para proteger o modelo de dominio de influencias externas.
11. **Core Domain** recebe o maior investimento de design e arquitetura.
12. **Arquitetura Hexagonal** para isolar o dominio de frameworks e infraestrutura.
13. **CQRS e Event Sourcing** em contextos de alta complexidade e necessidade de auditoria.
14. **Context Map** documentado e atualizado para todo projeto DDD.
15. **Modelos ricos em comportamento** — entidades com metodos de dominio, nao modelos anemicos.

---

## Anti-Patterns a Evitar

| Anti-Pattern | Problema |
|---|---|
| **Anemic Domain Model** | Entidades so com getters/setters; logica de negocio espalhada em Services. |
| **God Aggregate** | Aggregate enorme que engloba tudo; dificulta concorrencia e manutencao. |
| **Shared Database** | Dois Bounded Contexts acessam o mesmo schema de banco diretamente. |
| **Feature Envy** | Application Service com regras de negocio que pertencem ao dominio. |
| **Repository Generico** | `genericRepository.findBy(criteria)` que expoe toda a persistencia. |
| **Domain Model Leakage** | Modelos de dominio de um contexto vazam para outro sem ACL. |

---

*Fonte: Implementing Domain-Driven Design — Vaughn Vernon (Addison-Wesley, 2013)*
