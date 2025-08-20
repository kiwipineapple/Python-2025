# --------------------------------------------
# String-Definition in Python
# --------------------------------------------
# Variante 1: Mit doppelten Anführungszeichen
course = "Einführung in Python"

# Variante 2: Mit einfachen Anführungszeichen
course = 'Einführung in Python'

# Mehrzeilige Zeichenketten mit drei doppelten oder drei einfachen Anführungszeichen

nachricht1 = """
Hallo Sophia,

hier ist Marc, wie geht's dir?

Tschüß
"""


nachricht2 = '''
Hallo Marc,

mir geht's gut danke.

Tschüß
'''

print(nachricht1)
print(nachricht2)

# Escape zeichen bei eingebetteten Anführungszeichen
# print('Das ist Sophias's Blatt ' ) -> falsch
print("Das ist Sophias's Blatt")

print('Das ist Sophias \'s Blatt ' )

print('Das ist Sophias \'s Blatt \n Na und ' )
print('Das ist Sophias \'s Blatt \t Na und ' )

# ---------------------------------
# String Slicing
# -------------------------------------
course =        "Einführung in Python"
# Indexierung    0123456789 10 11 12.....19
# Indexierung    0123456789 10 11 12....-2-1
print(course) # Einführung in Python
# print das erste Zeichen
print(course[0])# E
print(course[-20])# E

print(course[9])# g

# # print das letzte Zeichen
print(course[19]) 
print(course[-1]) 

# Teil string
print(course[0:10])# Einführung
print(course[:10])# Einführung

print(course[14:20])# Python
print(course[-6:])# Python


print(course[-6])# P
print(course[2 -8])

# --------------------------------------------
# Zeichenketten-Verkettung (Concatenation)
# --------------------------------------------
name = 'Karoline' + 'Mueller'

vorname = 'Karoline' 
nachname = 'Mueller'

print(name)# KarolineMueller

name = 'Karoline ' + 'Mueller'
print(name)# Karoline Mueller

name = 'Karoline' + ' Mueller'
print(name)# Karoline Mueller

name = 'Karoline' + ' ' + 'Mueller'
print(name)# Karoline Mueller

name = 'Hallo'+' ' + vorname + ' ' +  nachname
print(name)# Hallo Karoline Mueller

# --------------------------------------------
# Formatierte Zeichenketten (f-Strings)
# --------------------------------------------
vorname = 'Kim' 
nachname = 'stark'
name = f'Hallo  {vorname} {nachname}, wie geht\' dir ?'
print(name)# Hallo Kim stark, wie geht's dir ?

# --------------------------------------------
# String-Funktionen und -Methoden
# --------------------------------------------

course = "Einführung in Python"
print('len(course): ',len(course))
# Groß- und Kleinschreibung
course = "   pyThon SpraCHe  "

print(course.upper())       # '   PYTHON SPRACHE'
print(course.lower())       # '   python sprache'
print(course.title())       # '   Python Sprache'
print(course.capitalize())  # '   python sprache'

# Leerzeichen entfernen
print(course.strip())       # "pyThon SpraCHe"

print(course.strip().capitalize()) # Python sprache

# Zeichen ersetzen
print(course.replace(' ', '_'))# ___pyThon_SpraCHe__
print(course.strip().replace(' ', '_')) # pyThon_SpraCHe


# Suche im Text (case-sensitiv)
course = "PyThon lanGuaGe with .py "
print(course.find('Py'))   # 0
print(course.find('py'))   # 22

# --------------------------------------------
# Escape-Zeichen
# --------------------------------------------

print('Beti sagt \'Guten Morgen\' alle zusammen!')   # Beti sagt 'Guten Morgen' ...
print("Beti sagt \"Guten Morgen\" alle zusammen!")  # Beti sagt "Guten Morgen" ...
print("Beti sagt \n Guten Morgen \n alle zusammen!") # Neue Zeilen
print("Beti sagt \n Guten Morgen \t alle zusammen!") # Tabulator
print("Beti sagt \\ Guten Morgen \\ alle zusammen!") # Backslashes
