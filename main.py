from tratamento.tratamento_dados_dia import Tratamento
from graficos.plot_graficos_dados import PlotGraficosDados
from processamento.processamento_dados import ProcessamentoDados

tratamento = Tratamento()
processamento = ProcessamentoDados()
plot = PlotGraficosDados()

# local_arquivo = (
#     r"C:\Users\Técnico em IA\PycharmProjects\PythonProject\60635000_Cotas.csv"
# )

data_frame = tratamento.tratar_dados(
    r"/Users/pablolemes/Documents/trabalho/IA - Senac/UC6-projeto-integrador/arquivos/estacao_60635000/60635000_Cotas.csv"
)

# teste_diario = processamento.media_diaria_cotas(data_frame, "01/2023", "06/2024")
# # teste_diario = processamento.media_mensal_cotas(data_frame, "01/2023", "06/2024")


# plot.plot_cotas(
#     df=teste_diario,
#     titulo="Média Diaria de jan/2023 a jun/2024",
#     intervalo_xticks=15,
#     group_by_month=False,
# )
