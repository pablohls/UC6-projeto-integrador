from graficos.plot_graficos_dados import PlotGraficosDados
from processamento.processamento_dados import ProcessamentoDados


processamento = ProcessamentoDados()
plot = PlotGraficosDados()
teste_diario = processamento.media_diaria_cotas("01/2023", "12/2023")

# plot.plot_cotas(teste_diario, "Vazão em setembro 2024")
plot.plot_cotas(teste_diario, "Cota em setembro 2024")
