# --------------------------------------------
# Benutzer-Eingabe mit input()
# --------------------------------------------

number1 = input("Gib die erste Zahl ein: ")# 2
number2 = input("Gib die zweite Zahl ein: ")#3

# --------------------------------------------
# Ausgabe der Eingaben
# --------------------------------------------
print("Die erste Zahl ist: ", number1)
print("Die zweite Zahl ist: ", number2)

# --------------------------------------------
# Hinweis: input() liefert immer einen String!
# --------------------------------------------
print(number1, type(number1))# 2 <class 'str'>

print(number1 + number2)#23

# --------------------------------------------
# Typkonvertierung in float (Kommazahl)
# --------------------------------------------
number1 = float(number1)
number2 = float(number2)
print(number1, type(number1))# 2.0 <class 'float'>
print(number1 + number2)# 5.0

# --------------------------------------------
# Beispiel: Namenseingabe und Begrüßung
# --------------------------------------------
first_name = input("Gib deinen Vornamen ein: ")
last_name = input("Gib deinen Nachnamen ein: ")

# Begrüßung mit Zeilenumbruch
print(f"Hallo,\n{first_name} {last_name}")