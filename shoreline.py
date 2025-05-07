import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Dados: média e desvio padrão de cada praia
praias = {
    "Conceição (Setor Oeste)": {"media": -3.95, "dp": 2.14},
    "Conceição (Setor Leste)": {"media": 2.82, "dp": 1.29},
    "Boldró": {"media": -4.04, "dp": 2.74},
    "Bode": {"media": -8.41, "dp": 2.39},
    "Quixambinha": {"media": -14.05, "dp": 6.24},
    "Cacimba": {"media": -0.18, "dp": 1.51},
}

# Intervalo comum para todas as curvas
x = np.linspace(-30, 10, 1000)

plt.figure(figsize=(12, 7))

# Cores para diferenciar as curvas
cores = plt.cm.viridis(np.linspace(0, 1, len(praias)))

for i, (nome, dados) in enumerate(praias.items()):
    media = dados["media"]
    dp = dados["dp"]
    y = norm.pdf(x, loc=media, scale=dp)
    
    # Curva
    plt.plot(x, y, label=nome, color=cores[i])
    
    # Linha vertical na média
    plt.axvline(media, linestyle='--', color=cores[i], alpha=0.6)
    
    # Anotação da média
    plt.annotate(f"Média = {media:.2f}",
                 xy=(media, norm.pdf(media, media, dp)),
                 xytext=(media + 1, norm.pdf(media, media, dp) + 0.005),
                 arrowprops=dict(arrowstyle="->", color=cores[i]),
                 fontsize=9, color=cores[i])

plt.title("Curvas de Densidade de Probabilidade Normal por Praia", fontsize=14)
plt.xlabel("Valor (ex: variação da linha de costa em metros)", fontsize=12)
plt.ylabel("Densidade de Probabilidade", fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
