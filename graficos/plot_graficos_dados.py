import matplotlib.pyplot as plt
import numpy as np


class PlotGraficosDados:

    def plot_cotas(self, df_resultado, titulo):

        # Ordenando os dados por Data para garantir a sequência correta
        df_resultado = df_resultado.sort_values(by="Data")

        # Criando os eixos
        x = df_resultado["Data"]
        y = df_resultado["Cota Média"]

        # Criando o gráfico principal
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, linestyle="-", color="blue", label="Cota Média")

        # Criando a linha de tendência
        x_num = np.arange(len(x))  # Criar valores numéricos para regressão
        coef = np.polyfit(x_num, y, 1)  # Regressão linear (grau 1)
        tendencia = np.poly1d(coef)(x_num)
        plt.plot(x, tendencia, linestyle="dotted", color="blue", label="Tendência")

        # Formatando o gráfico
        plt.xlabel("Dias")
        plt.ylabel("Cota Média")
        plt.title(titulo)
        plt.xticks(rotation=45)  # Rotacionar rótulos do eixo X para melhor visualização
        plt.legend()
        plt.grid(True)

        # Mostrar gráfico
        plt.show()
