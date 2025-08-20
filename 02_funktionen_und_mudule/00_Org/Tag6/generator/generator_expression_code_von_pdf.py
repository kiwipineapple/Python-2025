# List Comprehension
quadrate = [x * x for x in range(5)]
print(quadrate)  # Ausgabe: [0, 1, 4, 9, 16]




# Generator Expression – fast gleich, aber mit ()
quadrate_gen = (x * x for x in range(5))
print(quadrate_gen)  # Ausgabe: <generator object ...>

for wert in quadrate_gen:
    print(wert)

for wert in quadrate_gen:
    print(wert)
