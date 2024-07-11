# Pipeline de Extração de Dados usando Meltano, PostgreSQL e CSV

## Visão Geral
Este projeto implementa um pipeline de extração de dados utilizando Meltano, PostgreSQL e arquivos CSV. O pipeline consiste em duas etapas principais:

1. **Extração e Armazenamento Local**: O Meltano extrai dados de um banco de dados PostgreSQL (exceto a tabela `order_details`, que vem de um arquivo CSV) e os salva no disco local.
2. **Carregamento de Dados no PostgreSQL**: Os dados armazenados localmente são então carregados em um banco de dados PostgreSQL.

## Ferramentas e Tecnologias
- Airflow: Para agendamento e orquestração de tarefas
- Meltano: Para extração e carregamento de dados
- PostgreSQL: Banco de dados de origem e destino

## Estrutura do Pipeline
1. Extração de dados do PostgreSQL (exceto `order_details`)
2. Extração de dados do arquivo CSV (`order_details`)
3. Armazenamento local dos dados extraídos
4. Carregamento dos dados no PostgreSQL
5. Execução de consulta final para combinar dados

## Passos de Implementação
1. Configuração do Meltano:
   - Instalar Meltano
   - Configurar projeto Meltano
   - Adicionar taps e targets para PostgreSQL e CSV
   - Configurar pipelines de extração e carregamento
2. Configuração do Airflow:
   - Instalar e configurar Airflow
   - Criar DAGs para orquestração
   - Configurar dependências entre tarefas
3. Implementação do Pipeline:
   - Implementar pipeline de extração e armazenamento local
   - Implementar pipeline de carregamento de dados
   - Testar o pipeline completo

## Instruções de Execução
1. Configuração Inicial:
   - Instalar Meltano e Airflow
   - Configurar projeto Meltano e DAGs do Airflow
2. Execução Diária:
   - Iniciar Airflow
   - Monitorar execução dos DAGs
   - Verificar logs do Airflow para possíveis problemas
3. Consulta Final:
   - Executar uma consulta no PostgreSQL para combinar a tabela `orders` com os dados de `order_details`
   - Salvar o resultado da consulta em um arquivo CSV ou JSON

## Notas Adicionais
- Certifique-se de configurar corretamente as credenciais do banco de dados
- Monitore o uso de recursos durante a execução do pipeline
- Implemente tratamento de erros e notificações para falhas no pipeline