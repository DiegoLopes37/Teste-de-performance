import pandas as pd
import matplotlib.pyplot as plt

arquivos = [
    "resultados_10_stats.csv",
    "resultados_50_stats.csv",
    "resultados_100_stats.csv"
]

usuarios = []
medias = []
rps = []

for arquivo in arquivos:

    try:

        df = pd.read_csv(arquivo)

        total = df[df["Name"] == "Aggregated"]

        usuarios.append(
            arquivo.split("_")[1]
        )

        medias.append(
            total["Average Response Time"].values[0]
        )

        rps.append(
            total["Requests/s"].values[0]
        )

    except Exception as e:
        print(f"Erro ao ler {arquivo}: {e}")

plt.figure(figsize=(8,5))

plt.plot(usuarios, medias, marker="o")

plt.title("Tempo Médio de Resposta")

plt.xlabel("Usuários")

plt.ylabel("ms")

plt.grid()

plt.savefig(
    "grafico_tempo_resposta.png"
)

plt.close()

plt.figure(figsize=(8,5))

plt.plot(usuarios, rps, marker="o")

plt.title("Throughput")

plt.xlabel("Usuários")

plt.ylabel("Req/s")

plt.grid()

plt.savefig(
    "grafico_throughput.png"
)

plt.close()

print("Gráficos gerados com sucesso.")