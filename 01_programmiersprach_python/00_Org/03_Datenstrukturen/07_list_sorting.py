zahlen = [4, 2, 9, 1] 
print('vor dem Sorting')
print(zahlen)

print('nach Aufwärt  Sorting')
zahlen.sort()                # Aufsteigend 

print('nach dem Rückwärt  Sorting')
zahlen.sort(reverse=True)   # Absteigend 

zahlen = [4, 2, 9, 1] 
print('vor dem Sorting mit sorted')
print(zahlen)

neue_liste = sorted(zahlen)# # Kopie sortiert
print('nach dem Sorting mit sorted')
print(zahlen) # originale Liste bleibt unveränderbar
print(neue_liste)
