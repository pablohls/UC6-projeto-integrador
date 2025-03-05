import calendar
import pandas as pd


class ProcessamentoDados:
    """
    Classe responsável pelo processamento dos dados de cotas, incluindo o cálculo da média diária e mensal.

    Métodos:
    - media_diaria_cotas: Calcula a média diária das cotas dentro de um intervalo de tempo.
    - media_mensal_cotas: Calcula a média mensal das cotas dentro de um intervalo de tempo.
    """

    def media_diaria_cotas(self, df, data_inicial, data_final):
        """
        Calcula a média diária das cotas dentro do período especificado.

        Parâmetros:
        - df (DataFrame): DataFrame contendo as colunas "MesAno", "Dia" e "Cota".
        - data_inicial (str): Data de início no formato "MM/YYYY".
        - data_final (str): Data de fim no formato "MM/YYYY".

        Retorno:
        - DataFrame contendo a média diária das cotas no intervalo especificado, com as colunas "Data" e "Cota Média".
        """

        # Converte a coluna "MesAno" para o formato de data
        df["MesAno"] = pd.to_datetime(df["MesAno"], format="%m/%Y")

        # Converte a coluna "Dia" para número, tratando erros
        df["Dia"] = pd.to_numeric(df["Dia"], errors="coerce")

        # Converte as datas de início e fim para datetime
        data_inicial = pd.to_datetime(data_inicial, format="%m/%Y")
        data_final_dt = pd.to_datetime(data_final, format="%m/%Y")

        # Obtém o último dia do mês da data final para garantir o intervalo correto
        ultimo_dia = calendar.monthrange(data_final_dt.year, data_final_dt.month)[1]
        data_final = pd.Timestamp(
            year=data_final_dt.year, month=data_final_dt.month, day=ultimo_dia
        )

        # Calcula a data exata combinando "MesAno" e "Dia"
        df["Data"] = df["MesAno"] + pd.to_timedelta(df["Dia"] - 1, unit="D")

        # Filtra os dados dentro do intervalo especificado
        df_filtrado = df[(df["Data"] >= data_inicial) & (df["Data"] <= data_final)]

        # Calcula a média diária das cotas
        df_resultado = df_filtrado.groupby("Data")["Cota"].mean().reset_index()

        # Renomeia a coluna "Cota" para "Cota Média"
        df_resultado.rename(columns={"Cota": "Cota Média"}, inplace=True)

        return df_resultado  # Retorna o DataFrame com as médias diárias

    def media_mensal_cotas(self, df, data_inicial, data_final):
        """
        Calcula a média mensal das cotas dentro do período especificado.

        Parâmetros:
        - df (DataFrame): DataFrame contendo as colunas "MesAno" e "Cota".
        - data_inicial (str): Data de início no formato "MM/YYYY".
        - data_final (str): Data de fim no formato "MM/YYYY".

        Retorno:
        - DataFrame contendo a média mensal das cotas no intervalo especificado, com as colunas "Data" e "Cota Média".
        """

        # Converte a coluna "MesAno" para o formato de data
        df["MesAno"] = pd.to_datetime(df["MesAno"], format="%m/%Y")

        # Converte a coluna "Dia" para número, tratando erros
        df["Dia"] = pd.to_numeric(df["Dia"], errors="coerce")

        # Converte as datas de início e fim para datetime
        data_inicial = pd.to_datetime(data_inicial, format="%m/%Y")
        data_final_dt = pd.to_datetime(data_final, format="%m/%Y")

        # Obtém o último dia do mês da data final para garantir o intervalo correto
        ultimo_dia = calendar.monthrange(data_final_dt.year, data_final_dt.month)[1]
        data_final = pd.Timestamp(
            year=data_final_dt.year, month=data_final_dt.month, day=ultimo_dia
        )

        # Define a data como o primeiro dia do mês
        df["Data"] = df["MesAno"]
        df["Data"] = pd.to_datetime(df["Data"])

        # Filtra os dados dentro do intervalo especificado
        df_filtrado = df[(df["Data"] >= data_inicial) & (df["Data"] <= data_final)]

        # Calcula a média mensal das cotas
        df_resultado = df_filtrado.groupby("MesAno")["Cota"].mean().reset_index()

        # Renomeia as colunas para "Data" e "Cota Média"
        df_resultado.rename(
            columns={"Cota": "Cota Média", "MesAno": "Data"}, inplace=True
        )

        return df_resultado  # Retorna o DataFrame com as médias mensais
