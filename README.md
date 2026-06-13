# OrangeHRM Performance Test

## Descrição

Projeto desenvolvido para a disciplina de Testes de Software com foco em testes de performance utilizando Locust.

O sistema escolhido foi o OrangeHRM Demo:

https://opensource-demo.orangehrmlive.com/

## Objetivos

Avaliar:

- Tempo de resposta
- Throughput
- Escalabilidade
- Gargalos do sistema

## Cenários de Teste

| Cenário | Método |
|----------|---------|
| Login | POST |
| Dashboard | GET |
| Employee List | GET |
| Directory | GET |
| Search Employee | POST |
| Update Employee | POST |

## Cargas Testadas

- 10 usuários
- 50 usuários
- 100 usuários

## Tecnologias

- Python
- Locust
- Pandas
- Matplotlib
- ReportLab
- Docker

## Executar Localmente

Instalar dependências:

```bash
pip install -r requirements.txt