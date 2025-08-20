# --------------------------------------------
# Typumwandlung (Type Conversion) in Python
# --------------------------------------------
# Eingebaute Funktionen:
# int()   → Umwandlung in Ganzzahl
# float() → Umwandlung in Kommazahl
# str()   → Umwandlung in Zeichenkette

# --------------------------------------------
x = '2'
print(x, type(x))# 2 <class 'str'>

print(x*3)#222

# ------------------
# Umwandlung in Ganzzahl
x = int(x)
print(x, type(x))#2 <class 'int'>
print(x*3)# 6

# ------------------
# Umwandlung in Kommazahl

x = float(x)
print(x, type(x))#2 <class 'float'>
print(x*3)#6.0

# ----------------------
x = int(x)
# Zurück in eine Zeichenkette

x = str(x)
print(x, type(x))
print(x*4)#2222
