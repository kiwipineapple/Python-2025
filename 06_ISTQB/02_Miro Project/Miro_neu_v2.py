from item import *
from read_json import read_json


def create_pizza_menu(pizzas_input):
    return [Pizza(item['number'], item['name'], item['price'])
            for item in pizzas_input]


def create_auflauf_menu(auflaufs_input):
    return [Auflauf(item['number'], item['name'], item['price'])
            for item in auflaufs_input]


def print_pizza_menu(pizzas):
    print('Pizzen')
    print('=' * 10)
    for pizza in pizzas:
        print(pizza)


def print_auflauf_menu(auflaufs):
    print('Auflauf')
    print('=' * 10)
    for auf in auflaufs:
        print(auf)


def print_menu(pizzas, auflaufs):
    print('Wilkommen bei Miro restaurant ')
    print('=' * 10)
    print()
    print_pizza_menu(pizzas)
    print()
    print()
    print_auflauf_menu(auflaufs)


def find(menu, order_numer):
    for item in menu:
        if item.number == order_numer:
            return item
    return None


def bestellung(menu):
    print('\n\nWas möchsten Sie bestellen?')
    print('=' * 20)
    order_list = []
    while True:
        try:
            order_number = int(input('> '))
        except:
            print("Error input!")
        else:
            if order_number == 0:
                break

            found = find(menu, order_number)

            if not found:
                print('Leider bieten wir das nicht an.')
            else:
                order_list.append(found)

    return order_list


def print_quittung(order_list):
    print('\n\nQuittung')
    print('=' * 10)
    for order in order_list:
        print(order)

    sum = 0
    for order in order_list:
        sum += order.price
    print(f'\n\nDie Summe beträgt: {sum} €')
    print('\n\nVielen Dank für Ihren Besuch!')


if __name__ == '__main__':

    data = read_json()
    assert (len(data) == 2)
    pizzas_input = data[0]
    auflaufs_input = data[1]

    pizzas = create_pizza_menu(pizzas_input)
    auflaufs = create_auflauf_menu(auflaufs_input)

    print_menu(pizzas, auflaufs)

    menu = pizzas + auflaufs
    order_list = bestellung(menu)

    print_quittung(order_list)
