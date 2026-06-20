# OrangeHRM Performance Test

## Descrição

Projeto desenvolvido para a disciplina de Testes de Software com o objetivo de realizar testes de performance utilizando o Locust.

O sistema escolhido foi o OrangeHRM Demo:

https://opensource-demo.orangehrmlive.com/

## Objetivos

Avaliar o desempenho da aplicação sob diferentes níveis de carga, analisando:

* Tempo de resposta
* Throughput (requisições por segundo)
* Escalabilidade
* Possíveis gargalos

## Cenários de Teste

Foram implementados os seguintes cenários:

| Cenário         | Método |
| --------------- | ------ |
| Login           | POST   |
| Dashboard       | GET    |
| Employee List   | GET    |
| Directory       | GET    |
| Search Employee | POST   |
| Update Employee | POST   |

## Níveis de Carga

Os testes foram executados com:

* 10 usuários simultâneos
* 50 usuários simultâneos
* 100 usuários simultâneos

## Tecnologias Utilizadas

* Python 3.12
* Locust
* Pandas
* Matplotlib
* ReportLab
* Docker

## Estrutura do Projeto

```text
orangehrm_performance_test
│
├── locustfile.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── gerar_relatorio.py
|__ executa_testes.py
└── resultados/
```

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando o Locust

Modo interface web:

```bash
python -m locust -f locustfile.py --host https://opensource-demo.orangehrmlive.com
```

Acesse:

```text
http://localhost:8089
```

## Execução Headless

10 usuários:

```bash
python -m locust -f locustfile.py --headless -u 10 -r 2 --run-time 2m --host https://opensource-demo.orangehrmlive.com --csv resultados_10
```

50 usuários:

```bash
python -m locust -f locustfile.py --headless -u 50 -r 5 --run-time 2m --host https://opensource-demo.orangehrmlive.com --csv resultados_50
```

100 usuários:

```bash
python -m locust -f locustfile.py --headless -u 100 -r 10 --run-time 2m --host https://opensource-demo.orangehrmlive.com --csv resultados_100
```

## Execução de Múltiplos Cenários de Teste

Além da execução manual pelo Locust, o projeto possui o script 

```bash
python executar_testes.py
```
responsável por executar automaticamente diferentes cenários de carga e exportar os resultados para arquivos CSV.

Objetivo

Avaliar o comportamento do sistema sob diferentes níveis de concorrência para análise de:

Throughput (requisições por segundo)
Tempo médio de resposta
Percentis (P90, P95 e P99)
Escalabilidade
Saturação do sistema

## Geração dos Gráficos

Após executar os testes:

```bash
python gerar_relatorio.py
```

Serão gerados gráficos com os resultados coletados.

## Docker

Construir e executar:

```bash
docker-compose up --build

```
Subir o Locust com interface web (a pasta do projeto fica espelhada dentro do container, então tudo que for salvo lá aparece direto aqui):
```bash
docker compose up
```
Acesse http://localhost:8089

Rodar os 3 cenários automaticamente dentro do container:
```bash
docker compose run --rm locust python executar_testes.py
```

Gerar o relatório (gráficos + PDF) dentro do container:
```bash
docker compose run --rm locust python gerar_relatorio.py
```

```bash 

Teste 10 usuários
docker exec orangehrm_locust locust \
-f locustfile.py \
--headless \
-u 10 \
-r 2 \
--run-time 2m \
--host=https://opensource-demo.orangehrmlive.com \
--csv=resultados_10
```
```bash

Teste 50 usuários
docker exec orangehrm_locust locust \
-f locustfile.py \
--headless \
-u 50 \
-r 5 \
--run-time 2m \
--host=https://opensource-demo.orangehrmlive.com \
--csv=resultados_50
```

```bash

Teste 100 usuários
docker exec orangehrm_locust locust \
-f locustfile.py \
--headless \
-u 100 \
-r 10 \
--run-time 2m \
--host=https://opensource-demo.orangehrmlive.com \
--csv=resultados_100
```

## Autor

Diego  Vieira Lopes


