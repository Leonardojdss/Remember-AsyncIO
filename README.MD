# Remember-AsyncIO

## Repositório para lembrar as principais funções do asyncio

Repositório para lembrar as principais funções do asyncio em Python com exemplos práticos.

## Arquivos e Funcionalidades

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

## Conceitos Importantes

### Paralelo vs Concorrente
- **Concorrente**: Tarefas alternam rapidamente dando a impressão de execução simultânea
- **Paralelo**: Tarefas realmente executam ao mesmo tempo (em nossos exemplos, durante operações I/O)

### Principais Vantagens do AsyncIO
1. **Performance**: Reduz tempo total de execução para operações I/O
2. **Eficiência**: Melhor uso de recursos durante esperas
3. **Escalabilidade**: Permite lidar com muitas operações simultaneamente
