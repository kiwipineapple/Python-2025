
def menu():
    menu_number = [100, 101, 102, 200, 201]
    menu_name = ['Pizza Margeritta', 'Pizza Tunfisch',
                 'Pizza Fungi', 'Auflauf Nudeln', 'Auflauf Kartoffeln']
    menu_price = [5, 6, 7, 8, 9]
    print('Pizzen')
    print('=' * 10)
    for i in range(3):
        print(f'{menu_number[i]}. {menu_name[i]} {menu_price[i]}€')

    print('Auflauf')
    print('=' * 10)
    for i in range(3, 5):
        print(f'{menu_number[i]}. {menu_name[i]} {menu_price[i]}€')
    return menu_number, menu_name, menu_price


def bestellung(number):
    print('Was möchsten Sie bestellen?')
    print('=' * 20)
    order_list = []
    # print(number)
    while True:
        try:
            order_number = int(input('> '))
        except:
            print("Error input!")
        else:
            if order_number == 0:
                break
            elif order_number not in number:
                print('Leider bieten wir das nicht an.')
            else:
                order_list.append(order_number)

    return order_list


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
    number, name, price = menu()
    # print(number, name, price)
    oder_list = bestellung(number)
    # print(oder_list)
    quittung(oder_list, number, name, price)
