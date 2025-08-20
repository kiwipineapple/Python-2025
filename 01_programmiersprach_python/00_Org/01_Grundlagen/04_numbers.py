# --------------------------------------------
# Zahlentypen (Numerische Werte)
# --------------------------------------------
x = 2 # Integer (Ganzzahl)
y = 1.2 # Float(Kommazahl)

# --------------------------------------------
# Grundlegende mathematische Operationen
# --------------------------------------------
print(x + y)
print(x - y)
print(x * y)
print(x / y) # 1.6  Division:(Ergebnis ist immer float)
print(x // y) # 1   Ganzzahlige Division)
print(x % y)# 0.6000000000000001

# Potenz
print( x ** 2)# x hoch 2

# --------------------------------------------
# Mathematische Funktionen mit Modul math
# --------------------------------------------
import math

# Potenz (Alternative)

print( math.pow(x,2))
print(math.sqrt(25))
print(math.floor(2.9))# abrunden : 2
print(math.ceil(2.9)) # Aufrunden: 3

# --------------------------------------------
# Inkrementieren und Dekrementieren
# --------------------------------------------
x = 10
x = x + 3
print(x) # Ergebnis ist 13

x = x - 10
print(x) # # Ergebnis ist 3
# --------------------------------------------
# Kurzschreibweise (Kurzformen von Operationen)
# --------------------------------------------
x = 5
print(x + 5)

x += 5 # x = x+5
x -= 5 # x = x -5
x *= 5 # x = x *5
x /= 5 # x = x / 5
print(x)
