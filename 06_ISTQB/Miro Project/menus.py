
class Menu():
    """ Parent Class """

    def __init__(self, title, number, name, price) -> None:
        self.title = title
        self.number = number
        self.name = name
        self.price = price

    def print_menu(self):
        print(self.title)
        print('=' * 10)
        for i in range(len(self.number)):
            print(f'{self.number[i]}. {self.name[i]} {self.price[i]}€')


class Pizza(Menu):
    pass


class Auflauf(Menu):
    pass
