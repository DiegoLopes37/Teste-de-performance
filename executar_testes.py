import os

host = "https://opensource-demo.orangehrmlive.com"

cenarios = [
    (10, 2, "resultados_10"),
    (50, 5, "resultados_50"),
    (100, 10, "resultados_100")
]

for usuarios, ramp_up, nome in cenarios:

    comando = (
        f'python -m locust -f locustfile.py '
        f'--headless '
        f'-u {usuarios} '
        f'-r {ramp_up} '
        f'--run-time 2m '
        f'--host {host} '
        f'--csv {nome}'
    )

    print(f"\nExecutando cenário {usuarios} usuários...\n")
    os.system(comando)

print("\nTodos os testes concluídos!")