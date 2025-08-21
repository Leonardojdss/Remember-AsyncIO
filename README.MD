# Remember-AsyncIO

## Repositório para lembrar as principais funções do asyncio

Repositório para lembrar as principais funções do asyncio em Python com exemplos práticos.

## Arquivos e Funcionalidades

### 1. `factorial.py` - Execução Paralela de Cálculos
### 2. `tasks_paralele.py` - Tarefas Simultâneas  
### 3. `temporizer.py` - Timer Básico Assíncrono
### 4. `managing_subscriptions.py` - Sistema de Inscrições Concorrentes
### 5. `notification.py` - Sistema de Notificações Assíncronas
### 6. `orders.py` - Processamento de Pedidos Concorrente

---

### 1. `factorial.py` - Execução Paralela de Cálculos
**Funções asyncio utilizadas:**
- `asyncio.create_task()` - Cria tarefas assíncronas individuais
- `asyncio.gather()` - Executa múltiplas tarefas em paralelo
- `asyncio.sleep()` - Simula operações I/O não bloqueantes
- `asyncio.run()` - Executa o programa assíncrono

**Tipo de execução:** **Paralela/Concorrente**

Este arquivo demonstra como calcular fatoriais de múltiplos números simultaneamente. Cada cálculo é executado como uma tarefa independente, permitindo que todos rodem ao mesmo tempo ao invés de sequencialmente.

**Por que usar asyncio aqui?** 
- Permite calcular vários fatoriais simultaneamente
- O `asyncio.sleep(1)` simula operações que levariam tempo (como consultas a banco de dados)
- Reduz o tempo total de execução significativamente

### 2. `tasks_paralele.py` - Tarefas Simultâneas
**Funções asyncio utilizadas:**
- `asyncio.gather()` - Executa funções download() e analytics() simultaneamente
- `asyncio.sleep()` - Simula tempo de processamento
- `asyncio.run()` - Inicia o loop de eventos

**Tipo de execução:** **Paralela/Concorrente**

Simula um cenário onde você precisa fazer download de dados E analisar dados ao mesmo tempo. Ambas as operações rodam simultaneamente ao invés de uma após a outra.

**Por que usar asyncio aqui?**
- Download e análise podem acontecer ao mesmo tempo
- Reduz o tempo total de 4 segundos (2+2) para apenas 2 segundos
- Ideal para operações I/O que podem ser executadas independentemente

### 3. `temporizer.py` - Timer Básico Assíncrono
**Funções asyncio utilizadas:**
- `asyncio.sleep()` - Pausa não bloqueante
- `asyncio.run()` - Executa a função assíncrona

**Tipo de execução:** **Sequencial** (mas não bloqueante)

Exemplo básico de um timer assíncrono. Demonstra o uso fundamental do `asyncio.sleep()` para criar pausas que não bloqueiam o programa.

**Por que usar asyncio aqui?**
- O `asyncio.sleep()` é não bloqueante, permitindo que outras tarefas rodem durante a pausa
- Base para entender como funciona a programação assíncrona

### 4. `managing_subscriptions.py` - Sistema de Inscrições Concorrentes
**Funções asyncio utilizadas:**
- `asyncio.create_task()` - Cria tarefas individuais para cada inscrição
- `asyncio.gather()` - Processa todas as inscrições simultaneamente
- `asyncio.run()` - Executa o programa principal

**Tipo de execução:** **Paralela/Concorrente**

Simula um sistema de inscrições em cursos onde múltiplos usuários tentam se inscrever simultaneamente. O sistema verifica disponibilidade de vagas e processa todas as inscrições em paralelo.

**Por que usar asyncio aqui?**
- Processa múltiplas inscrições simultaneamente
- Simula comportamento real de sistemas web com múltiplos usuários
- Demonstra como lidar com recursos compartilhados (vagas limitadas) em ambiente concorrente

### 5. `notification.py` - Sistema de Notificações Assíncronas
**Funções asyncio utilizadas:**
- `asyncio.create_task()` - Cria tarefa para cada notificação
- `asyncio.gather()` - Envia todas as notificações simultaneamente
- `asyncio.run()` - Inicia o sistema de notificações

**Tipo de execução:** **Paralela/Concorrente**

Sistema que envia notificações para múltiplos usuários considerando preferências individuais (VIP, notificações ativadas/desativadas). Todas as notificações são processadas simultaneamente.

**Por que usar asyncio aqui?**
- Envia notificações para todos os usuários ao mesmo tempo
- Ideal para sistemas que precisam notificar muitos usuários rapidamente
- Demonstra processamento condicional em ambiente assíncrono

### 6. `orders.py` - Processamento de Pedidos Concorrente
**Funções asyncio utilizadas:**
- `asyncio.create_task()` - Cria tarefa para cada pedido
- `asyncio.gather()` - Processa todos os pedidos simultaneamente
- `asyncio.run()` - Executa o sistema de processamento

**Tipo de execução:** **Paralela/Concorrente**

Sistema de e-commerce que processa múltiplos pedidos simultaneamente, verificando pagamento e estoque para cada pedido. Simula o fluxo completo de validação de pedidos.

**Por que usar asyncio aqui?**
- Processa múltiplos pedidos ao mesmo tempo
- Reduz tempo total de processamento em sistemas de alto volume
- Demonstra validações múltiplas (pagamento + estoque) em ambiente assíncrono

## Conceitos Importantes

### Paralelo vs Concorrente
- **Concorrente**: Tarefas alternam rapidamente dando a impressão de execução simultânea
- **Paralelo**: Tarefas realmente executam ao mesmo tempo (em nossos exemplos, durante operações I/O)

### Principais Vantagens do AsyncIO
1. **Performance**: Reduz tempo total de execução para operações I/O
2. **Eficiência**: Melhor uso de recursos durante esperas
3. **Escalabilidade**: Permite lidar com muitas operações simultaneamente
4. **Sistemas Concorrentes**: Ideal para simular comportamentos de aplicações web reais
5. **Processamento em Lote**: Excelente para processar múltiplos itens (pedidos, notificações, etc.)
