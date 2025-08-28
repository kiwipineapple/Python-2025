from menus import *
import greetings as gt
from order import *


def quittung(order_list, number, name, price):
    print('Quittung')
    print('=' * 10)
    sum = 0
    for num in order_list:
        x = number.index(num)
        # print(x)
        print(f'{number[x]}. {name[x]} {price[x]}€')
        sum += price[x]
    print(f'Die Summe beträgt: {sum}€')


if __name__ == '__main__':
    gt.greeting()

    pizza_list = [100, 101, 102]
    pizza_name = ['Pizza Margeritta', 'Pizza Tunfisch', 'Pizza Fungi']
    pizza_price = [5, 6, 7]
    pizza_menu = Pizza('Pizzen', pizza_list, pizza_name, pizza_price)
    pizza_menu.print_menu()

    auflauf_list = [200, 201]
    auflauf_name = ['Auflauf Nudeln', 'Auflauf Kartoffeln']
    auflauf_price = [8, 9]
    pizza_menu = Pizza('Auflauf', auflauf_list, auflauf_name, auflauf_price)
    pizza_menu.print_menu()

    oder_list = bestellung(pizza_list, auflauf_list)
    print(oder_list)
    # quittung(oder_list, number, name, price)
