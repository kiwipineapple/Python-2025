# --------------------------------------------
#  Vergleichsoperatoren
# --------------------------------------------
print('10 > 3  ->', 10 > 3) # True
print('10 < 3  ->', 10 < 3) # False
print('10 == 3  ->', 10 == 3) # False
print('10 >= 3  ->', 10 >= 3) # True
print('10 <= 3  ->', 10 <= 3) # False
print('10 != 3  ->', 10 != 3)# True

print('-'*40)

# --------------------------------------------
# Logische Operatoren: and / or
# --------------------------------------------

x = 10
y = 20

# AND (Beide Bedingungen müssen wahr sein)
print( x == 10 and y == 20)  # True and True → True
print( x == 11 and y == 20)   # False and True → False
print( x != 11 and y == 20)  # True and True → True
print( x == 11 and y != 20)  # False and False -> False

print('-' * 40)

# OR (Eine Bedingung muss wahr sein)
print( x == 10 or y == 20)  # True or True → True
print( x == 11 or y == 20)   # False or True → True
print( x != 11 or y == 20)  # True or True → True
print( x == 11 or y != 20)  # False or False -> False

# --------------------------------------------
# NOT-Operator
# --------------------------------------------
anwesend = True
print( not anwesend)

print('-' * 40)

# --------------------------------------------
# IN-Operator (Mitgliedschaft prüfen)
# --------------------------------------------
course = 'Python Schulung'

print('Python' in course) # True (exakt enthalten)
print('python' in course) # False (Groß-/Kleinschreibung beachten!)