from tratamento.tratamento_dados_dia import Tratamento
import calendar
import pandas as pd


class ProcessamentoDados:

    def get_dados(self):
        tratamento = Tratamento()

        dados_tratados = tratamento.tratar_dados()
        return dados_tratados

    def media_diaria_cotas(self, data_inicial, data_final):
        """
        Retorna um DataFrame contendo todas as datas dentro do intervalo especificado,
        com a média das cotas para cada dia.

        Parâmetros:
        - data_inicial: string no formato "MM/YYYY".
        - data_final: string no formato "MM/YYYY".

        Retorna:
        - DataFrame com as colunas: ["Data", "Cota Média"]
        """

        df = self.get_dados()

        # Convertendo 'MesAno' para datetime
        df["MesAno"] = pd.to_datetime(df["MesAno"], format="%m/%Y")

        # Convertendo 'Dia' para inteiro
        df["Dia"] = pd.to_numeric(df["Dia"], errors="coerce")

        # Convertendo as datas fornecidas para datetime
        data_inicial = pd.to_datetime(data_inicial, format="%m/%Y")

        data_final_dt = pd.to_datetime(data_final, format="%m/%Y")
        ultimo_dia = calendar.monthrange(data_final_dt.year, data_final_dt.month)[1]
        data_final = pd.Timestamp(
            year=data_final_dt.year, month=data_final_dt.month, day=ultimo_dia
        )

        # Criando uma nova coluna de Data completa
        df["Data"] = df["MesAno"] + pd.to_timedelta(df["Dia"] - 1, unit="D")

        # Filtrando os dados no intervalo desejado
        df_filtrado = df[(df["Data"] >= data_inicial) & (df["Data"] <= data_final)]

        # Agrupando por Data e calculando a média das cotas para cada dia
        df_resultado = df_filtrado.groupby("Data")["Cota"].mean().reset_index()

        # Renomeando a coluna
        df_resultado.rename(columns={"Cota": "Cota Média"}, inplace=True)

        return df_resultado

    def media_mensal_cotas(self, data_inicial, data_final):
        """
        Retorna um DataFrame contendo a média das cotas para cada mês dentro do intervalo especificado.
        """
        df = self.get_dados()

        # Convertendo 'MesAno' para datetime
        df["MesAno"] = pd.to_datetime(df["MesAno"], format="%m/%Y")

        # Convertendo 'Dia' para inteiro
        df["Dia"] = pd.to_numeric(df["Dia"], errors="coerce")

        # Convertendo as datas fornecidas para datetime
        data_inicial = pd.to_datetime(data_inicial, format="%m/%Y")

        data_final_dt = pd.to_datetime(data_final, format="%m/%Y")
        ultimo_dia = calendar.monthrange(data_final_dt.year, data_final_dt.month)[1]
        data_final = pd.Timestamp(
            year=data_final_dt.year, month=data_final_dt.month, day=ultimo_dia
        )

        # Criando uma nova coluna de Data completa
        df["Data"] = df["MesAno"]
        df["Data"] = pd.to_datetime(df["Data"])

        # Filtrando os dados no intervalo desejado
        df_filtrado = df[(df["Data"] >= data_inicial) & (df["Data"] <= data_final)]

        # Agrupando por Data e calculando a média das cotas para cada mês
        df_resultado = df_filtrado.groupby("MesAno")["Cota"].mean().reset_index()

        # Renomeando a coluna
        df_resultado.rename(columns={"Cota": "Cota Média"}, inplace=True)

        return df_resultado
