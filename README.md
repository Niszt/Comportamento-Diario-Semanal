# Gerenciador de Rotina Semanal - Padrao Strategy

Este projeto em Python implementa um gerenciador de rotina utilizando conceitos de Orientacao a Objetos. O objetivo principal é demonstrar a aplicação de padroes de projeto para resolver o problema de delegacao de comportamentos dinamicos, eliminando completamente o uso de cadeias extensas de condicionais (`if/elif/else`).

##  Funcionalidades

O sistema atende aos seguintes requisitos funcionais:
* **Consulta Automatica:** Obtem a data atual do sistema operacional e executa a estrategia correspondente ao dia de hoje.
* **Consulta Manual:** Permite consultar a estrategia de um dia especifico informado manualmente pelo usuario.
* **Resiliencia a Falhas:** Responde de forma segura a consultas de dias invalidos ou não cadastrados sem interromper a execução do programa.
* **Recomendações Dinâmicas:** Cada dia possui um nivel de prioridade (ALTA, EMDIA, BAIXA) e uma mensagem personalizada embutida em sua estrategia.

##  Padroes de Projeto Utilizados

Este projeto foi desenhado com base em boas praticas de arquitetura de software, aplicando os seguintes padroes:

* **Strategy (GoF):** Utilizado para encapsular o comportamento de cada dia da semana em classes separadas (`EstrategiaSegundaFeira`, `EstrategiaTercaFeira`, etc.) que assinam um mesmo contrato (a interface `EstrategiaDia`). Um componente de Contexto (`GerenciadorRotina`) delega a execucao para a estrategia apropriada atraves de um mapeamento em dicionario.
* **Null Object Pattern:** Implementado através da classe `EstrategiaInvalida`. Garante que, caso o usuario insira um dia inexistente (ex: "dia-falso") ou o sistema consulte um dia nao mapeado, o programa retorne um comportamento neutro e seguro ao inves de estourar um erro ou excecao (`KeyError` ou `NullReference`).

##  Como Executar

1. Clone o repositorio.
2. Abra o terminal na pasta do projeto.
3. Execute o script principal:

```bash
python main.py
