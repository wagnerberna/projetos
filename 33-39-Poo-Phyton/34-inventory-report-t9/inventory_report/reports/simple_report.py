from datetime import date


class SimpleReport:
    @staticmethod
    def generate(dados):
        map_data_fabricacao = list(
            map(lambda el: el["data_de_fabricacao"], dados)
        )
        min_data_fabricacao = min(map_data_fabricacao)
        # print(map_data_fabricacao)
        # print(min_data_fabricacao)

        data_atual = str(date.today())
        map_data_validade = list(map(lambda el: el["data_de_validade"], dados))
        filter_data_validade = list(
            filter(lambda el: el >= data_atual, map_data_validade)
        )
        min_data_validade = min(filter_data_validade)
        # print(map_data_validade)
        # print(filter_data_validade)
        # print(min_data_validade)

        map_nome_empresa = list(map(lambda el: el["nome_da_empresa"], dados))
        max_emp = max(map_nome_empresa)
        # print(map_nome_empresa)
        # print(max_emp)

        return (
            f"Data de fabricação mais antiga: {min_data_fabricacao}\n"
            f"Data de validade mais próxima: {min_data_validade}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {max_emp}\n"
        )


# RETORNOS:

# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA

# Teste local:
def stock():
    return [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]


dados_teste = stock()
# print(dados_teste)
teste = SimpleReport.generate(dados_teste)
# print(teste)
