words = ["apple", "banana", "cherry", "grape", "date", "fig"]


sorted_normal = sorted(words)
print(sorted_normal)

# Sortiere nach dem letzten Zeichen in jedem Wort
sorted_by_last_char = sorted(words, key= lambda x: x[-1])
print(sorted_by_last_char)
# Die sorted()-Funktion verwendet diese zurückgegebenen Werte von lambda Funktion - letzten Buchstaben, um die Reihenfolge zu bestimmen.
# Bei gleichen letzten Buchstaben bleibt die ursprüngliche Reihenfolge erhalten (stabile Sortierung).