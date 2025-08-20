print('Hallo')
print()
'''
Thema: print()
'''

"""
Datum: 23/06/2025
"""

print('1.Basics')
print('2.Control Flows')

#verschiedene Arten von Trennenlinien
print('-'*17)
print(''*17)

print('A', end='--->')
print('B')
print('A', 'B')
print('A', 'B', sep=',')
print('A', 'B', 'C', 123, sep='#')

#=======================
#Kobination
print()
print('A', 'B',sep='*', end='-')
#=========================

#---------------
print()
name = 'Maria'
jahr = 2025

print(f'Hallo {name}, willcome in {jahr}')
print('2.Alternative')
print('Hallo {}, willcome in {}'.format(name, jahr))