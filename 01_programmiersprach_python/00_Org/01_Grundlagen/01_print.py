# =================================
# Einzeilige Kommentare mit #
#=================================
# ich bin ein Kommentar


print('Hallo')# ich bin eine print() Funktion
# ich bin auch ein Kommentar

# =================================
# Mehzeilige Kommentare mit ( """ """)(''' ''')
#=================================
""" 
Thema : print()
Datum: 23/06/2025
Author: Asmae Bethi
"""

'''
Thema : print()
Datum: 23/06/2025
Author: Asmae Bethi
'''

# =================================
# print() Anweisungen
# ==================================
print('Hallo Welt!')
print("~~~~~~~~~~~~")
print()
print('willkommen bei der WBS')
print('Inhalt')
print('-------')
print()

# Leere Zeilke erstellen
print()

# Inhaltverzeichnis:
# ~~~~~~~~~~~~~~~~~
print('1. Basics')
print('2. Control Flows')

# Verschiedene Arten von Trennlinien
print("~~~~~~~~~~~~~~~~~")
print('~' * 17)
print('=' * 20)

# ==============================
# Mehrere Argumente in print()
# ==========================
print('Hallo', 'Sophia')# Ausgabe Hallo Sophia
print('Hallo', 'Sophia','im Jahr', 2025)# Automatisch mit Leerzeichen getrennt

# ==============================
# Sonder parameter von print()
# ==========================
# 'end' bestimmt, wie die Zeile endet (statt Zeilenumbruch)
print()
print('A', end= '-->')
print('B')
print('C', 'D')

# 'sep' definiert das Trennzeichen zwischen Argumenten
print()
print('A', 'B') #A B
print('A', 'B', sep=',')# A,B
print('A , B','c',123, sep='#')

# Kombination von 'sep' und 'end'
print()
print('A', 'B', sep = '*',    end = '=')

# =======================================
# Weitere Varianten der Ausgabe
# ==========================================
print()
print()
name = "Maria"
jahr = 2050

print(f'Hallo {name}, Willkommen im Jahr {jahr}!')# Ausgabe : Hallo Sophia, Willkommen im Jahr 2025!


# alternative
print('2. Alternative')
print('Hallo {}, Willkommen im Jahr {}!'.format(name, jahr))

# Alternative (veraltet aber noch gültig)
print('3. Alternative')
print('Hallo %s, Willkommen im Jahr %d!' % (name, jahr))




























