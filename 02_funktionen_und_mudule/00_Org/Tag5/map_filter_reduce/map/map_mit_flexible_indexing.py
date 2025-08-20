# Originale Listen
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
list3 = [100, 200, 300, 400]

# Definiere den Startindex
start_index = 1

# Schneide die Listen zu, sodass sie ab dem gewünschten Index starten
sliced_list1 = list1[start_index:]
sliced_list2 = list2[start_index:]
sliced_list3 = list3[start_index:]

# Verwende map() mit den zugeschnittenen Listen
result = map(lambda x, y, z: x + y + z, sliced_list1, sliced_list2, sliced_list3)

# Konvertiere das Ergebnis in eine Liste und zeige es an
print(list(result))  # Ausgabe: [222, 333, 444]
