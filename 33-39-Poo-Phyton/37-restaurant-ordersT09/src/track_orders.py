from collections import Counter


class TrackOrders:
    # constructor
    def __init__(self):
        self.orders = []
        self.index = 0
        # self.customer_orders = []

    # Atributo p/ iterar sobre a lista
    # Não é requisito
    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.orders[self.index]
            self.index += 1
            return item
        # interrompe quando acaba a lista
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f"{self.orders}"

    # pega itens por index
    def __getitem__(self, index):
        return self.orders[index]

    # alterar itens:
    def __setitem__(self, index, valor):
        self.orders[index] = valor

    # deletar item:
    def __delitem__(self, index):
        del self.orders[index]

    # quantidade itens array orders
    def __len__(self):
        return len(self.orders)

    # adiciona novas ordens
    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    # filtra dados do cliente
    def get_costumer_info(self, costumer):
        filter_costumer = list(
            filter(lambda el: el[0] == costumer, self.orders)
        )
        return filter_costumer

    # Prato favorito por cliente - Refatorado
    def get_most_ordered_dish_per_costumer(self, costumer):
        filter_costumer = list(
            filter(lambda el: el[0] == costumer, self.orders)
        )
        meals_client = list(map(lambda el: el[1], filter_costumer))
        print(filter_costumer)
        print(meals_client)
        meal_most_common = Counter(meals_client).most_common(1)
        print(meal_most_common)

        return meal_most_common[0][0]

    # Prato favorito por cliente - Refatorado
    # @classmethod
    # def get_most_ordered_dish_per_costumer(cls, costumer):
    #     print(costumer)
    #     costumer_info = cls.get_costumer_info(costumer=costumer)
    #     print(costumer_info)
    #     return costumer_info

    # Pratos nunca pedidos por cada cliente
    def get_never_ordered_per_costumer(self, costumer):
        meals_all = set(map(lambda el: el[1], self.orders))
        print(meals_all)
        filter_costumer = list(
            filter(lambda el: el[0] == costumer, self.orders)
        )
        meals_client = set(map(lambda el: el[1], filter_costumer))
        print(meals_client)
        meals_never_requested = meals_all - meals_client
        return meals_never_requested

    # dia nunca visitado pelo cliente
    def get_days_never_visited_per_costumer(self, costumer):
        filter_costumer = list(
            filter(lambda el: el[0] == costumer, self.orders)
        )
        days_client = set(map(lambda el: el[2], filter_costumer))
        print(days_client)
        days_week = {"segunda-feira", "terça-feira", "sabado"}
        days_client_never_stay = days_week - days_client
        return days_client_never_stay

    # Dia mais movimentado
    def get_busiest_day(self):
        meals_all = list(map(lambda el: el[2], self.orders))
        print(meals_all)
        day_most_common = Counter(meals_all).most_common(1)
        print(day_most_common)
        return day_most_common[0][0]

    # Dia menos movimentado
    def get_least_busy_day(self):
        meals_all = list(map(lambda el: el[2], self.orders))
        print(meals_all)
        day_least_common = Counter(meals_all).most_common()
        print(day_least_common)
        return day_least_common[-1][0]


if __name__ == "__main__":
    # testes
    # instancia objeto:
    order_test = TrackOrders()

    # quantidade orders:
    print(len(order_test))

    # add order:
    order_test.add_new_order("wagner", "vegetariano", "sabado")
    order_test.add_new_order("aline", "vegetariano", "segunda")
    order_test.add_new_order("jorge", "frango", "domingo")
    order_test.add_new_order("wagner", "vegetariano", "sabado")
    order_test.add_new_order("wagner", "X-Vegan", "segunda")
    order_test.add_new_order("wagner", "Pizza Marguerita", "segunda")

    print(len(order_test))
    # necessário implementar iterador
    print(order_test)
    # get item
    print(order_test[1])
    # set item
    order_test[1] = ("aline", "vegetariano", "domingo")
    print(order_test[1])

    del order_test[3]
    print(order_test)
    order_test.add_new_order("wagner", "vegetariano", "segunda")

    print("dados do cliente:")
    print(order_test.get_costumer_info("wagner"))
    # Prato favorito por cliente
    print("---Prato favorito por cliente---")
    print(order_test.get_most_ordered_dish_per_costumer("wagner"))
    # Pratos nunca pedidos por cada cliente
    print("---Pratos nunca pedidos por cada cliente---")
    print(order_test.get_never_ordered_per_costumer("wagner"))
    # dia nunca visitado pelo cliente
    print("---dia nunca visitado pelo cliente---")
    print(order_test.get_days_never_visited_per_costumer("wagner"))
    # Dia mais movimentado
    print("---Dia mais movimentado---")
    print(order_test.get_busiest_day())
    print("---Dia menos movimentado---")
    print(order_test.get_least_busy_day())