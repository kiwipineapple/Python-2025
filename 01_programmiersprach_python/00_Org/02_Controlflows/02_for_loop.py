
##  Abschnitt 1: Zahlen ausgeben

# einzeln mit print()
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)

print('-'*40)

for num in [1,2,3,4,5,6,7]:
    print(num)


print('-'*40)    

# einzeln mit print() 1,2,3,4,5 6 7
print(1, end=',')
print(2, end=',')
print(3, end=',')
print(4)


print('-'*40)

for num in [1,2,3,4,5,6,7]:
    print(num, end= ' ')

print()

#  Abschnitt 2: Begrüßung von Teilnehmenden

# Wiederholender Code
print('Hallo Marc')
print('Welches BKG?')
print('Python Kenntnissen')
print()
print('Hallo Mich')
print('Welches BKG?')
print('Python Kenntnissen')
print()
print('Hallo Marie')
print('Welches BKG?')
print('Python Kenntnissen')

print()

# Alternative
for teilnehmende in ['Marc','Michi','Marie']:
    print('Hallo', teilnehmende)
    print('Welches BKG?')
    print('Python Kenntnissen')

    print()
    
print()


#  Abschnitt 3: Verwendung von range()    

# Beispiele mit range()
range(10) # 0 1 2 3 4 5 6 7 8 9
range(1,8) # 1 2 3 4 5 6 7
range(0,11,2) #0 2 4 6 8 10 range( start index, last index +1, step)



for num in range(10):
    print(num, end=' ')

print()
for num in range(1,8):
    print(num, end=' ')


print()
for num in range(0,11,2):
    print(num, end=' ') # 0 2 4 6 8 10


print('+'*40)
counter = 1

for teilnehmende in ['Marc','Michi','Marie']:
    print(f'[{counter}].\t{teilnehmende}')
    counter+= 1 # counter = counter + 1

    

    print()

#  Abschnitt 4: Verschachtelte Schleifen
for farbe in ['Rot', 'Grün', 'Gelb']:

    for form in ['Kreis', 'Quadrat', 'Dreieck']:
        print(f'{farbe} {form}')   

    print()


# Abschnitt 5: Schleifensteuerung mit break und continue

# break: Schleife beenden, wenn num == 5
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
