
class Item():
    """ Parent Class """

    def __init__(self, number, name, price) -> None:
        self.number = number
        self.name = name
        self.price = price

    def __str__(self):
        # for i in range(len(self.number)):
        return f'{self.number}. {self.name} {self.price}€'


class Pizza(Item):
    pass
    # self.radius = radius


class Auflauf(Item):
    pass
