# class Bank:
#     def __init__(self, name, number, balance):
#         self.__name = name
#         self.__number = number
#         self.__balance = balance
#
#     def print_balance(self):
#         print(f'Ваш баланс {self.__balance}, Номер ваши карты: {self.__number}')
#     def change_balance(self, money):
#         self.__balance += money
#
# client = Bank('Вася', '1111 2222 3333 4444', 1000)
# client.print_balance()
# client.change_balance(2000)
# client.print_balance()
class Bank:
    def __init__(self, name, number, balance):
        self.__name = name
        self.__number = number
        self.__balance = balance

    def print_balance(self):
        print(f'Ваш баланс {self.__balance}, Номер ваши карты: {self.__number}')
    def change_balance(self, money):
        self.__balance += money
    @property
    def happy_balance(self):
        return self.__balance
    @happy_balance.setter
    def happy_balance(self, new_balance):
        self.__balance = new_balance
    @happy_balance.deleter
    def happy_balance(self):
        self.__balance = 0


client = Bank('Вася', '1111 2222 3333 4444', 1000)
print('Текущий баланс: ', client.happy_balance)
