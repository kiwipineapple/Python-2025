# Übung 2: Uhrzeit mit verschachtelten Schleifen
for stunde in range(24):
    for minute in range(60):
        for sekunde in range(60):
            print(f"{stunde}:{minute}:{sekunde}")

# Übung 3: Arbeiten mit Zahlen (einfach)
UPPER_LIMIT = 20

print("Alle Zahlen von 1 bis", UPPER_LIMIT)
for i in range(1, UPPER_LIMIT + 1):
    print(i)

print("Alle ungeraden Zahlen:")
for i in range(1, UPPER_LIMIT + 1):
    if i % 2 != 0:
        print(i)

print("Alle geraden Zahlen:")
for i in range(1, UPPER_LIMIT + 1):
    if i % 2 == 0:
        print(i)

summe_ungerade = 0
summe_gerade = 0

for i in range(1, UPPER_LIMIT + 1):
    if i % 2 != 0:
        summe_ungerade += i
    else:
        summe_gerade += i

print("Summe aller ungeraden Zahlen:", summe_ungerade)
print("Summe aller geraden Zahlen:", summe_gerade)

# Übung 4: Arbeiten mit Zahlen (mit Grenzen)
LOWER_LIMIT = 5
UPPER_LIMIT = 20

print(f"Alle Zahlen von {LOWER_LIMIT} bis {UPPER_LIMIT}")
for i in range(LOWER_LIMIT, UPPER_LIMIT + 1):
    print(i)

print("Alle ungeraden Zahlen:")
for i in range(LOWER_LIMIT, UPPER_LIMIT + 1):
    if i % 2 != 0:
        print(i)

summe_ungerade_bereich = 0
for i in range(LOWER_LIMIT, UPPER_LIMIT + 1):
    if i % 2 != 0:
        summe_ungerade_bereich += i

print("Summe aller ungeraden Zahlen:", summe_ungerade_bereich)
