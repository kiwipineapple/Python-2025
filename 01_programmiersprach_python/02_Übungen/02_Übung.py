import math

name = input('Hallo, wie ist Ihr Name: ')
print(f'Willkommen {name}')

weight = float(input('Ihre Köpergewicht in kg: '))
tall = float(input('Ihre Köpergröße in Meter: '))
# bmi = weight/(tall**2)
bmi = weight/(math.pow(tall,2))
bmi = round(bmi, 2)
print(f'Ihre BMI ist {bmi}')


# name = input('Hallo, wie ist Ihr Name: ')
# print(f'Willkommen {name}')
# glasbottle = int(input('Wie viele Glasflasche haben Sie? '))
# plasticbottle = int(input('Wie viele Plastikflasche haben Sie? '))
# pfandwert = glasbottle * 0.15 + plasticbottle * 0.25
# print(f'Ihre Pfandwert ist {pfandwert} euro.')