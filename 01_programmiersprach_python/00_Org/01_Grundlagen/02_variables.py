# -------------------
# Variablen erstellen
# -------------

v_integer = 5 # Ganzzahl
v_float = 5.5 # Kommazahl
v_string = 'Python' # Zeichenkette mit einfachen Enführungszeichen
v_string2 = "python" # Zeichenkette mit doppelten Enführungszeichen
v_boolean = True # Wahrheitswert
v_boolean2 = False # Wahrheitswert

# ----------------------------
# Werte Anzeigen
#___________________________
print('v_integer ist gleich ') # ausgabe : v_interger
print(v_integer)

print('v_integer ist gleich ', end=':') # ausgabe : v_interger
print(v_integer)
print()

print(f'v_float = {v_float}')

# ----------------------------------
# Datentypen anzeigen
# ---------------------------
print()
print( 'Datatype of the variable v_integer is ', type(v_integer)  )
print()
print(  type(v_float)  )

# -------------------
# Dynamische Typisierung
# -------------------------
x = 5
print(x, type(x)) # 5 <class 'int'>

x = 'Python'
print(x, type(x)) # Python <class 'str'>  

# ---------------------------
# Variablennamen
# ----------------------------
# python ist case-sensitive
# 'course' und 'Course' sind zwei verschiedene Variablen
course = 'JAVA'
Course = 'Python'

print(course)
print(Course)


# Konstante (Konvention: nur Großbuchstaben)
CONSTANR_NAME = 'Python Course'

# ------------
#Schlechte Benenneung vermeiden
#------------
c1 = 'Python'
j ='JAVA'