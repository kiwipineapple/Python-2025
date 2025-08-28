
def bestellung(pizza_list, auflauf_list):
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
            elif order_number not in pizza_list and order_number not in auflauf_list:
                print('Leider bieten wir das nicht an.')
            else:
                order_list.append(order_number)

    return order_list
