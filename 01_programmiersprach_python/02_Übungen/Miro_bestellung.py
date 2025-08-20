print('\nWillkommen bei Miro restaurant')
print('=================')
print('Pizzen')
print('======')


pizza_liste = [[100, 'Pizza Margeritta', 5], [101, 'Pizza Tunfisch', 6], [102, 'Pizza Fungi', 7]]
auflauf_liste = [[200, 'Auflauf Nudeln', 8], [201,'Auflauf Kartoffeln', 9]]


for gericht in pizza_liste:
    print(f'{gericht[0]}. {gericht[1]} {gericht[2]}€')

print('\nAuflauf')
print('======')


for gericht in auflauf_liste:
    print(f'{gericht[0]}. {gericht[1]} {gericht[2]}€')


print('\nWas möchten Sie bestellen?')
print('='*30)
order_nummmer = []
order_name = []
order_price = []



while True:
    oder = int(input('> '))
    if oder == 0:
        break
    gefunden = False
    for gericht in pizza_liste:
        if oder == gericht[0]:
            order_nummmer.append(gericht[0])
            order_name.append(gericht[1])
            order_price.append(gericht[2])
            gefunden = True
            break
    for gericht in auflauf_liste:
        if oder == gericht[0]:
            order_nummmer.append(gericht[0])
            order_name.append(gericht[1])
            order_price.append(gericht[2])
            gefunden = True
            break
    if not gefunden:
        print('Leider bieten wir das nicht an')


print('Quittung')
print('=======')
sum = 0

for index in range(len(order_nummmer)):
    print(f'{order_nummmer[index]}. {order_name[index]} {order_price[index]}€')
    sum += order_price[index]
print(f'Die Summe Beiträge ist {sum}€')
print('Vielen Dank für Ihre Besuche!')