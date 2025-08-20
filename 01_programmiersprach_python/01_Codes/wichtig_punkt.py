name = "Maria"
jahr = 2050

print(f'Hallo {name}, Willkommen im Jahr {jahr}!')# Ausgabe : Hallo Sophia, Willkommen im Jahr 2025!

# Mehrzeilige Zeichenketten mit drei doppelten oder drei einfachen Anführungszeichen
nachricht1 = """
Hallo Sophia,

hier ist Marc, wie geht's dir?

Tschüß
"""
print(nachricht1)


course = "   pyThon SpraCHe  "
print(course.strip())       # "pyThon SpraCHe"
print(course.strip().capitalize()) # Python sprache

course = "PyThon lanGuaGe with .py "
print(course.find('Py'))   # 0

print("Beti sagt \n Guten Morgen \t alle zusammen!") # Tabulator
print("Beti sagt \\ Guten Morgen \\ alle zusammen!") # Backslashes

x = 2
y = 1.2
print(x // y) # 1   Ganzzahlige Division)
print(x % y)# 0.6000000000000001
print(round(x/y, 2))

import math
print(math.pow(x,2))
print(math.sqrt(25))


"""
  Schleifenarten in Python:

- for-Schleifen sind ideal für durchlaufbare Datenstrukturen,
  wenn die Anzahl der Iterationen bekannt ist.

- while-Schleifen sind nützlich für Bedingungen, bei denen
  die Iteration von einer logischen Prüfung abhängt und
  nicht von einer festen Anzahl.
"""

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

obst = ["Apfel", "Banane", "Kirsche"]

# Iteration über Listen
for frucht in obst: 
    print(frucht) 



for i in range(len(obst)): 
    print(f"Index {i}: {obst[i]}")

index = obst.index("Kirsche") 
print(f"Kirsche bei Index {index}")