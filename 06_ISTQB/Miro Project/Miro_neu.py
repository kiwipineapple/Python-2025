
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
    oder_list = []
    # print(number)
    while True:
        oder_number = int(input('> '))
        if oder_number == 0:
            break
        elif oder_number not in number:
            print('Leider bieten wir das nicht an.')
        else:
            oder_list.append(oder_number)

    return oder_list


def quittung(oder_list, number, name, price):
    print('Quittung')
    print('=' * 10)
    sum = 0
    for num in oder_list:
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
