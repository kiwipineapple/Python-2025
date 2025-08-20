# counter = 1

# for teilnehmende in ['Marc','Michi','Marie']:
#     print(f'[{counter}].\t{teilnehmende}')
#     counter+= 1 # counter = counter + 1

# for farbe in ['Rot', 'Grün', 'Gelb']:

#     for form in ['Kreis', 'Quadrat', 'Dreieck']:
#         print(f'{farbe} {form}')   

#     print()

for num in range(10):
    if num == 5:
        break
    print(num)

print()

# continue: num == 5 überspringen
for num in range(10):
    if num == 5:
        print('Banana')
        continue
    print(num)