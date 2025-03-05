import numpy as np
import matplotlib.pyplot as plt


class PlotGraficosDados:
    """
    Classe responsável por gerar gráficos a partir dos dados de cotas.

    Métodos:
    - plot_cotas: Plota um gráfico de linhas com as cotas médias ao longo do tempo.
    """

    def plot_cotas(
        df, titulo, intervalo_xticks=10, group_by_month=True, show_tendencia=False
    ):
        """
        Plota um gráfico de cotas médias ao longo do tempo.

        Parâmetros:
        - df (DataFrame): DataFrame contendo as colunas "Data" e "Cota Média".
        - titulo (str): Título do gráfico.
        - intervalo_xticks (int, opcional): Define o espaçamento entre os valores do eixo X. Padrão é 10.
        - group_by_month (bool, opcional): Se True, agrupa os dados por mês. Caso contrário, exibe os dias acumulados. Padrão é True.
        - show_tendencia (bool, opcional): Se True, adiciona uma linha de tendência ao gráfico. Padrão é False.

        Retorno:
        - Nenhum. O gráfico gerado é exibido na tela.
        """

        # Ordena os dados pela coluna "Data" para garantir a sequência correta
        df_resultado = df.sort_values(by="Data")

        # Define os valores do eixo X (tempo) e do eixo Y (cota média)
        x = df_resultado["Data"]
        y = df_resultado["Cota Média"]

        if group_by_month:
            # Agrupa os dados por mês e calcula a média da cota para cada período
            df_resultado["AnoMes"] = x.dt.to_period("M")
            df_agrupado = (
                df_resultado.groupby("AnoMes")["Cota Média"].mean().reset_index()
            )

            eixo_x = df_agrupado["AnoMes"].astype(
                str
            )  # Converte para string para exibição no eixo X
            y = df_agrupado["Cota Média"]  # Atualiza os valores do eixo Y
            xlabel = "Meses"  # Define o rótulo do eixo X
        else:
            # Calcula os dias acumulados desde a primeira data do intervalo
            eixo_x = (x - x.iloc[0]).dt.days + 1
            xlabel = "Dias acumulados"

        # Cria a figura e plota a linha principal do gráfico
        plt.figure(figsize=(10, 5))
        plt.plot(eixo_x, y, linestyle="-", color="blue", label="Cota Média")

        if show_tendencia:
            # Adiciona uma linha de tendência ao gráfico usando regressão linear
            x_num = np.arange(len(y))
            coef = np.polyfit(x_num, y, 1)
            tendencia = np.poly1d(coef)(x_num)
            plt.plot(
                eixo_x, tendencia, linestyle="dotted", color="blue", label="Tendência"
            )

        # Configura os rótulos do eixo X, exibindo apenas alguns valores para evitar sobreposição
        plt.xticks(
            ticks=eixo_x[::intervalo_xticks],
            labels=eixo_x[::intervalo_xticks],
            rotation=45,
        )

        # Configura os rótulos dos eixos e o título do gráfico
        plt.xlabel(xlabel)
        plt.ylabel("Cota Média")
        plt.title(titulo)
        plt.legend()

        # Exibe o gráfico
        plt.show()
