# HW 2 OOP
#Тема: ООП — наследование, инкапсуляция и итерация

# Базовый класс
class Order:
    def __init__(self, amount):
        self._amount = amount  

    def get_amount(self):
        return self._amount

    def get_type(self):
        return "Order"


# Наследование
class OnlineOrder(Order):
    def get_type(self):
        return "OnlineOrder"


class OfflineOrder(Order):
    def get_type(self):
        return "OfflineOrder"


# Итерация
class OrderList:
    def __init__(self, orders):
        self._orders = orders  # список заказов

    def __iter__(self):
        return iter(self._orders)  # возвращаем итератор по списку


# Использование
orders = OrderList([
    OnlineOrder(1000),
    OfflineOrder(500),
    OnlineOrder(2000)
])

for order in orders:
    print(f"Type: {order.get_type()}, Amount: {order.get_amount()}")
