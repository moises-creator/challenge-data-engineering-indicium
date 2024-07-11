# `Documentação - Resolução do Desafio Tech Engenharia de Dados da Incidium`

Esse projeto tem o intuito de explorar a ferramenta Meltano, orquestrar o pipeline usando Airflow. Seu objetivo principal é extrair as informações de duas bases de dados, um CSV e um banco de dados Postgres, salvar em um diretório local e logo em seguida salvar todas as informações em um banco de dados Postgres.


## `1° Passo - Preparar o ambiente:`

* `Baixe este repositório para prosseguir:` https://github.com/moises-creator/challenge-data-engineering-incidium.git

* `Crie o ambiente virtual e ative-o na pasta raíz do projeto(estou usando pip e venv):`https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

* `Navegue até a pasta:` *desafio-incidium/etl_pipeline*

## `2° Passo - Instalar e criar o banco de dados Postgres:`
* `Comando para instalar:`sudo apt install postgresql postgresql-contrib
* `Comando para iniciar o banco:`sudo systemctl start postgresql.service
* `Comando para entrar no banco:`sudo -u postgres psql
* `Se você estiver logado com a conta postgres, crie o banco diretamente:` createdb Northwind 
* `para conectar no banco use:` \connect
* `altere a senha para poder referenciar a sua senha nas variáveis de ambiente:`ALTER USER postgres PASSWORD 'NovaSenha';
* `Confirmar a alteração de senha:`\p
* `copie e cole a query disponibilizada pelo desafio:`https://github.com/techindicium/code-challenge/blob/main/data/northwind.sql

## `3° Passo - Instalar o Meltano:`

* `Verifique se existe atualizações no sistema:` *pip install --upgrade pip*  
* `Instale o Meltano usando pip:` *pip install meltano*  
* `Verifique se foi instalado:` *meltano --version*  


## `4° Passo - Instalar extratores e carregadores:`

`Obs:` *Como vamos utilizar duas bases de dados diferentes, vamos usar um extrator e carregador para CSV e outro para Postgres. Lembrando estar na pasta desafio-incidium/etl_pipeline*


## `tap-csv`
#### `extractor`
* `Adicione no terminal:` *meltano add extractor tap-csv* 
* `Configure o tap-csv usando --intractive:` *meltano config tap-csv set --interactive*
* `Teste se as configurações do extrator são válidas:` *meltano config tap-csv test*  

#### `loader`
* `Adicione no terminal:` *meltano add loader target-csv* 
* `Configure o target-csv usando --intractive:` *meltano config target-csv set --interactive*


## `tap-postgres`
#### `extractor`
* `Adicione no terminal:` *meltano add extractor tap-postgres* 
* `Configure o tap-postgres usando --intractive:` *meltano config tap-postgres set --interactive*
* `Teste se as configurações do extrator são válidas:` *meltano config tap-postgres test*  

#### `loader`
* `Adicione no terminal:` *meltano add loader target-postgres* 
* `Configure o target-postgres usando --intractive:` *meltano config target-postgres set --interactive*



## `5° Passo - Configurar variáveis de ambiente:`
TAP_POSTGRES_HOST='localhost'
TAP_POSTGRES_PORT='5432'
TAP_POSTGRES_USER='postgres'
TAP_POSTGRES_PASSWORD='postgres'
TAP_POSTGRES_DATABASE='Northwind'

TARGET_POSTGRES_HOST='localhost'
TARGET_POSTGRES_PORT='5432'
TARGET_POSTGRES_USER='postgres'
TARGET_POSTGRES_PASSWORD='postgres'
TARGET_POSTGRES_DATABASE='Northwind'
PROJECT_PATH='/home/analista/desafio-incidium/etl_pipeline/'




## `6° Passo - Instalar e configurar Airflow:`


* `Adiciona a utility airflow ao meltano:` meltano add utility airflow

* `Inicializa o airflow:` meltano invoke airflow:initialize

* `Cria um usuario dentro do airflow:` meltano invoke airflow users create -u admin@localhost -p password --role Admin -e admin@localhost -f admin -l admin

* `Executar o airflow scheduler junto com o webapp:` meltano invoke airflow standalone

* `Foi elaborada uma dag onde executa os subprocessos do meltano, para mais detalhes verifique a pasta orchestrate/airflow/dags/dag_pipeline_meltano.py:`

`Obs: `Ao executar o airflow, o pipeline sera executado automaticamente, pode acompanhar a execucao acessando `localhost:3000` no Browser.




### *Esse projeto foi elaborado em contratempo com meus estudos para tirar a certificação Professional Data Engineer do Google, pretendo realizar possíveis melhorias. Gratidão pela oportunidade de aprender algo novo e extremamente útil!.*