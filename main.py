from tratamento.tratamento_dados_dia import Tratamento
from graficos.plot_graficos_dados import PlotGraficosDados
from processamento.processamento_dados import ProcessamentoDados

tratamento = Tratamento()
processador = ProcessamentoDados()
plot = PlotGraficosDados()

# local_arquivo = (
#     r"C:\Users\Técnico em IA\PycharmProjects\PythonProject\60635000_Cotas.csv"
# )

df_tratado = tratamento.tratar_dados(
    r"/Users/pablolemes/Documents/trabalho/IA - Senac/UC6-projeto-integrador/arquivos/estacao_60635000/60635000_Cotas.csv"
)


# Define o intervalo de tempo desejado
data_inicial = "01/2023"
data_final = "12/2023"

# Calcula a média diária
df_media_diaria = processador.media_diaria_cotas(df_tratado, data_inicial, data_final)

# Calcula a média mensal
df_media_mensal = processador.media_mensal_cotas(df_tratado, data_inicial, data_final)

# Plota os dados diários
# PlotGraficosDados.plot_cotas(
#     df_media_diaria,
#     "Cota Diária",
#     intervalo_xticks=10,
#     group_by_month=False,
#     show_tendencia=True,
# )

# Plota os dados mensais
PlotGraficosDados.plot_cotas(
    df_media_mensal,
    "Cota Mensal",
    intervalo_xticks=1,
    group_by_month=True,
    show_tendencia=False,
)
