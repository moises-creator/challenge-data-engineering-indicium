






meltano add utility airflow

meltano invoke airflow:initialize

meltano invoke airflow users create -u admin@localhost -p password --role Admin -e admin@localhost -f admin -l admin


#adiciona a utility airflow ao meltano
meltano add utility airflow

#Inicializa o airflow
meltano invoke airflow:initialize

#Cria um usuario dentro do airflow
meltano invoke airflow users create -u admin@localhost -p password --role Admin -e admin@localhost -f admin -l admin

#Executar o airflow scheduler junto com o webapp
meltano invoke airflow standalone


#Ao executar o airflow, o pipeline sera executado automaticamente, pode acompanhar a execucao acessando localhost:3000 no navegador