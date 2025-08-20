# Ursprüngliche Liste
lst = [0, 1, 2, 3, 4, 5]

# Anfangs-Slicing-Parameter
start = 1
stop = 4
step = 1

# Erstellen eines slice-Objekts
my_slice = slice(start, stop, step)

# my_slice1 = slice(1, 4, 1)

# Erstes Ergebnis mit dem ursprünglichen slice
result1 = lst[my_slice]
print("Erstes Ergebnis:", result1)  # Ausgabe: [1, 2, 3]

# Dynamische Änderung des stop-Parameters, um ein weiteres Element einzuschließen
stop += 1
my_slice = slice(start, stop, step)

# Zweites Ergebnis mit dem geänderten slice
result2 = lst[my_slice]
print("Zweites Ergebnis:", result2)  # Ausgabe: [1, 2, 3, 4]
