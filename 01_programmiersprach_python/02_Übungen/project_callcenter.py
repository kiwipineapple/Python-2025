print('Welcome by Vodafone')
print('[1] EN\n[2] DE')

# i = 1
# if i <= 3:
#     spa = int(input('Language/Sprache >'))
#     if spa == 1:
#         firstname = input('first name: ')
#         lastname = input('last name: ')
#         print(f'Welcome {firstname} {lastname}!')
#     elif spa == 2:
#         firstname = input('Vorname: ')
#         lastname = input('Nachname: ')
#         print(f'Welcome {firstname} {lastname}!')
#     else:
#         print('Sorry, user language should be 1 or 2.')
        
#     i = i + 1


while True:
    i = 1
    spa = int(input('Language/Sprache >'))
    if spa == 1:
        firstname = input('first name: ')
        lastname = input('last name: ')
        print(f'Welcome {firstname} {lastname}!')
        break
    elif spa == 2:
        firstname = input('Vorname: ')
        lastname = input('Nachname: ')
        print(f'Welcome {firstname} {lastname}!')
        break
    elif spa > 2:
        print('Sorry, user language should be 1 or 2.')
        i += i
    elif i > 3:
        print('All the chance used.')
    break
        

