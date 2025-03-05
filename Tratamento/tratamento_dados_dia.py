# Colunas nessa formatação: EstacaoCodigo     Data   hora Dia   Cota
import pandas as pd


class Tratamento:
    def tratar_dados(self, local_arquivo):
        """
        Processa e trata os dados de um arquivo CSV contendo informações de cota de uma estação hidrométrica.

        Parâmetros:
        local_arquivo (str): Caminho do arquivo CSV a ser lido.

        Retorna:
        pd.DataFrame: DataFrame tratado com as colunas organizadas e dados formatados corretamente.
        """
        # Lendo o arquivo CSV, ignorando as 11 primeiras linhas do cabeçalho e separando por ponto e vírgula
        df = pd.read_csv(
            local_arquivo,
            encoding="latin1",  # Define a codificação para suportar caracteres especiais
            header=11,  # Ignora as primeiras 11 linhas do arquivo
            sep=";",  # Define o separador como ponto e vírgula
        )

        # Identifica e remove colunas relacionadas ao "Status"
        colunas_status = [col for col in df.columns if "Status" in col]
        df = df.drop(colunas_status, axis=1)

        # Remove colunas desnecessárias para a análise
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

        # Ajusta a coluna "Data" para conter apenas mês e ano
        df["Data"] = df["Data"].str[3:]

        # Remove linhas onde a coluna "hora" está vazia
        df = df.dropna(subset=["hora"])

        # Identifica colunas que contêm valores de cota
        colunas_cota = [col for col in df.columns if "Cota" in col]

        # Converte os dados para um formato longo, agrupando por estação, mês/ano e hora
        df = df.melt(
            id_vars=["EstacaoCodigo", "Data", "hora"],  # Mantém essas colunas fixas
            value_vars=colunas_cota,  # Colunas com valores de cota serão agrupadas
            var_name="Dia",  # Nova coluna que identificará os dias
            value_name="Cota",  # Nova coluna que armazenará os valores das cotas
        )

        # Remove a palavra "Cota" dos valores da coluna "Dia" para deixar apenas o número do dia
        df["Dia"] = df["Dia"].str.replace("Cota", "")

        # Remove linhas onde a coluna "Cota" está vazia
        df = df.dropna(subset=["Cota"])

        # Renomeia a coluna "Data" para "MesAno" para melhor compreensão
        df = df.rename(columns={"Data": "MesAno"})

        return df
