# ERP Bridges

## 🇺🇸 English Version

An ERP hub designed to unify and analyze data from multiple reports and external systems, creating a single, trusted source of information.

### 📖 About The Project

In the business world, data is often scattered across multiple sources: spreadsheets, marketplace reports, payment systems, etc. ERP Bridges was created to solve this challenge by unifying this data into a single source of truth.

The heart of the system is a well-planned database, ensuring that information is consistent, easy to track, and ready to generate valuable insights. A good design now prevents major headaches in the future.

### 🏛️ Core Architecture: Hub and Spoke

To meet the need of unifying distinct data sources, a **Hub and Spoke** architecture was chosen. This model is ideal for centralizing information in an organized and scalable way.

Think of a bicycle wheel:
- **HUB (the center part):** This is our `BuyOrder` table (Purchase Order). It represents the central, immutable event.
- **SPOKES (the rods connecting to the center):** These are the tables that add context to the Hub, such as `Customer`, `OrderDetail`, `PaymentType`, etc.

#### Advantages of this Architecture
* **✅ Centralization:** All data from different sources connect to a single order (the Hub). This makes tracking the entire lifecycle of a sale complete and cohesive.
* **✅ Scalability:** Need to integrate a new report from a marketplace or a logistics system? Just create a new "spoke" (a new model) and connect it to the `BuyOrder` Hub, without disrupting the existing structure. Simple, modular, and efficient.

### 🧩 Key Design Patterns Adopted

In addition to the overall architecture, other patterns were applied to ensure database robustness:

* **Lookup Tables:** Models like `PaymentType` and `Status` were separated into their own tables. This prevents typos and inconsistencies (e.g., "Approved" vs "approved"), facilitates filter creation, and optimizes data analysis.
* **Surrogate Keys:** We use Django's auto-incrementing `id` as the primary key in all models. Identifiers from external systems (like `order_number`) are stored as unique, indexed fields but not as primary keys. This decouples our system, ensuring its integrity and stability even if the external system has issues or changes its ID patterns.

### 🛠️ Technology Stack & Tools

* **Backend:** Python, Django, Django REST Framework
* **Database:** PostgreSQL (suggested)
* **Design & Diagramming:** [dbdiagram.io](https://dbdiagram.io) - An excellent free and intuitive online tool for designing database schemas.

---

## 🇧🇷 Versão em Português

Um ERP centralizador projetado para unificar e analisar dados de múltiplos relatórios e sistemas externos, criando uma fonte única e confiável de informação.

### 📖 Sobre o Projeto

No mundo dos negócios, os dados costumam estar espalhados por diversas fontes: planilhas, relatórios de marketplaces, sistemas de pagamento, etc. O ERP Bridges nasceu para resolver este desafio, unificando esses dados em um único lugar.

O coração do sistema é um banco de dados bem planejado, que garante que a informação seja consistente, fácil de rastrear e pronta para gerar análises valiosas. Um bom design agora evita dores de cabeça gigantes no futuro.

### 🏛️ Arquitetura Principal: Hub and Spoke

Para atender à necessidade de unificar fontes de dados distintas, a arquitetura escolhida foi a **Hub and Spoke**. Este modelo é ideal para centralizar informações de forma organizada e escalável.

Pense em uma roda de bicicleta:
- **HUB (o cubo no centro):** É a nossa tabela `BuyOrder` (Ordem de Compra). Ela representa o evento central e imutável.
- **SPOKES (os raios que se conectam ao centro):** São as tabelas que adicionam contexto ao Hub, como `Customer` (Cliente), `OrderDetail` (Detalhes do Pedido), `PaymentType` (Forma de Pagamento), etc.

#### Vantagens desta Arquitetura
* **✅ Centralização:** Todos os dados de diferentes fontes se conectam a um único pedido (o Hub). Isso torna o rastreamento do ciclo de vida de uma venda completo e coeso.
* **✅ Escalabilidade:** Precisa integrar um novo relatório de um marketplace ou um sistema de logística? Basta criar um novo "raio" (um novo model) e conectá-lo ao Hub `BuyOrder`, sem impactar a estrutura que já existe. Simples, modular e eficiente.

### 🧩 Padrões de Design Adotados

Além da arquitetura geral, outros padrões foram aplicados para garantir a robustez do banco de dados:

* **Tabelas de Consulta (Lookup Tables):** Models como `PaymentType` e `Status` foram separados em suas próprias tabelas. Isso evita erros de digitação e inconsistências (ex: "Aprovado" vs "aprovado"), facilita a criação de filtros e otimiza a análise de dados.
* **Chaves Surrogadas (Surrogate Keys):** Utilizamos o `id` auto-incrementado do Django como chave primária em todos os models. Os identificadores de sistemas externos (como o `order_number`) são armazenados como chaves únicas, mas não primárias. Isso desacopla nosso sistema, garantindo sua integridade e estabilidade mesmo que o sistema externo tenha falhas ou mude seus padrões de ID.

### 🛠️ Tecnologias e Ferramentas

* **Backend:** Python, Django, Django REST Framework
* **Frontend:** Django Templates, Tailwindcss, HTMX, AlpineJS, Lucide Icons
* **Banco de Dados:** PostgreSQL (sugerido)
* **Design e Diagramação:** [dbdiagram.io](https://dbdiagram.io) - Uma excelente ferramenta online e gratuita para desenhar esquemas de banco de dados de forma intuitiva.

