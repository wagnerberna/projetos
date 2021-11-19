import csv
from collections import Counter


def read_data(path):
    print(path)
    if path.endswith("csv"):
        with open(path, "r") as file:
            data = list(csv.reader(file))
            return data
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


# print(read_data("data/orders_1.csv"))
# read_data("data/orders_1.csv")


def get_client_info(client, data):
    # print(data)
    # print(data[0][0])
    data_client = list(filter(lambda el: el[0] == client, data))
    # print(data_client)
    # client_details = list(map(lambda el:
    # {"meal": el[1], "day": el[2]}, data))
    # print(client_details)
    return data_client


# print(get_client_info("maria"))


def get_all_meals(data):
    # print(data)
    all_meals = list(map(lambda el: el[1], data))
    # print(all_meals)
    return all_meals


# print(get_all_meals())


def get_meals_by_client(client, data):
    data_client = get_client_info(client, data)
    # el se refere a cada array interno
    meals_client = list(map(lambda el: el[1], data_client))
    # print(meals_client)
    return meals_client


# Qual o prato mais pedido por 'maria'?
def most_requested_meal(client, data):
    meals_client = get_meals_by_client(client, data)
    meal_most_common = Counter(meals_client).most_common(1)
    # print(meal_most_common)
    return meal_most_common[0][0]


# print(most_requested_meal("maria"))


# Quantas vezes 'arnaldo' pediu 'hamburguer'?
def number_orders_meal(client, meal, data):
    meals_client = get_meals_by_client(client, data)
    filter_mel = list(filter(lambda el: el == meal, meals_client))
    # print(filter_mel)
    meal_count = len(filter_mel)
    return meal_count


# print(number_orders_meal("arnaldo", "hamburguer"))


# Quais pratos 'joao' nunca pediu?
def never_requested_meals(client, data):
    meals_all = set(get_all_meals(data))
    # print(meals_all)
    meals_client = set(get_meals_by_client(client, data))
    # print(meals_client)
    meals_never_requested = meals_all - meals_client
    return meals_never_requested


# print(never_requested_meals("joao"))


def filter_days_client(client, data):
    data_client = get_client_info(client, data)
    days_client = list(map(lambda el: el[2], data_client))
    return days_client


# print(filter_days_client("joao"))

# Quais dias 'joao' nunca foi na lanchonete?
def days_client_never_stay_in_restaurant(client, data):
    days_client = set(filter_days_client(client, data))
    # print(days_client)
    days_week = {"segunda-feira", "terça-feira", "sabado"}
    days_client_never_stay = days_week - days_client
    return days_client_never_stay


# print(days_client_never_stay_in_restaurant("joao"))


def analyze_log(path_to_file):
    data = read_data(path_to_file)
    maria_info_meals = most_requested_meal("maria", data)
    arnaldo_info_meals = number_orders_meal("arnaldo", "hamburguer", data)
    joao_info_meals = never_requested_meals("joao", data)
    joao_info_days = days_client_never_stay_in_restaurant("joao", data)
    result = (
        f"{maria_info_meals}\n"
        f"{arnaldo_info_meals}\n"
        f"{joao_info_meals}\n"
        f"{joao_info_days}"
    )
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(result)


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
    analyze_log("data/orders_3.csv")
    analyze_log("data/orders_1.txt")
