# Ausgangsliste
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Neue Elemente, die eingefügt werden sollen
new_elements = [100, 101]

# Slicing verwenden, um die neuen Elemente in die Liste einzufügen
my_list[5:5] = new_elements

print(my_list)  # Ausgabe: [0, 1, 2, 3, 4, 100, 101, 5, 6, 7, 8, 9]

"""
Slicing-Bereich: my_list[5:5] spezifiziert die Position direkt nach 
dem Element mit Index 4 (also nach der 4), vor dem Element mit Index 5 (also vor der 5).
"""

my_list[5:9] = [200, 201, 202]
print(my_list) # Ausgabe: [0, 1, 2, 3, 4, 200, 201, 202, 7, 8, 9]
