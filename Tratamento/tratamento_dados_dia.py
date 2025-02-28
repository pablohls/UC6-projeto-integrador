import pandas as pd

# Colunas nessa formatação: EstacaoCodigo     Data   hora Dia   Cota

local_arquivo = (
    r"C:\Users\Técnico em IA\PycharmProjects\PythonProject\60635000_Cotas.csv"
)

# local_arquivo = r"/Users/pablolemes/Documents/trabalho/IA - Senac/UC6-projeto-integrador/arquivos/estacao_60635000/60635000_Cotas.csv"

df = pd.read_csv(
    local_arquivo,
    encoding="latin1",
    header=11,
    sep=";",
)

colunas_status = [col for col in df.columns if "Status" in col]

# Deleta as colunas encontradas
df = df.drop(colunas_status, axis=1)

colunas = [
    "NivelConsistencia",
    "MediaDiaria",
    "TipoMedicaoCotas",
    "Maxima",
    "Minima",
    "Media",
    "DiaMaxima",
    "DiaMinima",
    "MediaAnual",
]
df = df.drop(colunas, axis=1)

df["Data"] = df["Data"].str[3:]

df = df.dropna(subset=["hora"])
colunas_cota = [col for col in df.columns if "Cota" in col]
# print(colunas_cota)
df = df.melt(
    id_vars=["EstacaoCodigo", "Data", "hora"],
    value_vars=colunas_cota,
    var_name="Dia",
    value_name="Cota",
)

df["Dia"] = df["Dia"].str.replace("Cota", "")
df = df.dropna(subset=["Cota"])
df = df.rename(columns={"Data": "MesAno"})

print(df)
