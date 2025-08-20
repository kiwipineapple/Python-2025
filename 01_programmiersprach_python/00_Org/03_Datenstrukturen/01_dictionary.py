# Dictionary definieren
user = {'id': 50, 'name': 'Lina', 'PLZ': '12345'}
print(user, type(user))

# Dictionary mit verschachtelten Werten
users = [
    {'id': 50, 'name': 'Lina', 'PLZ': '12345'},
    {'id': [1, 1, 4], 'name': {'fn': 'Anna', 'ln': 'Stark'}, 'PLZ': '3456'}
]

# Alternative Definition mit dict()
user = dict(id=50, name='Lina', PLZ='12345')
print(user, type(user))

# Wert ändern
user['name'] = 'Ana'
print(user)

# Neues Schlüssel-Wert-Paar hinzufügen
user['stadt'] = 'Hamburg'
print(user)

# Nach Schlüssel suchen
print(user['stadt'])  # Direkter Zugriff
print(user.get('stadt'))  # Zugriff mit get()
print(user.get('location'))  # None, wenn Schlüssel nicht vorhanden
print(user.get('location', 'Kein Schlüssel für location'))

# Schlüssel löschen
user.pop('stadt')
print(user)

# Wert beim Löschen speichern
first_name = user.pop('name')
print(user)
print(first_name)

# Prüfen ob Schlüssel existiert
if 'id' in user.keys():
    print('Id-Schlüssel existiert')

# Alle Schlüssel anzeigen
for key in user.keys():
    print(key)

# Alle Werte anzeigen
for val in user.values():
    print(val)

# Schlüssel-Wert-Paare anzeigen
for key, val in user.items():
    print(key, val)