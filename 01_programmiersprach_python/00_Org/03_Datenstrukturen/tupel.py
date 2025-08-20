obst_tupel = ("Apfel", "Banane", "Kirsche")

obst_tupel = ('Apfel', 'Banane', 'Kirsche')

print(obst_tupel, type(obst_tupel))# ('Apfel', 'Banane', 'Kirsche') <class 'tuple'>

# Tupel von Zahlen
numbers = (1,2,3,4,4,5,6,0,8,9,5)
print(numbers, type(numbers))


tupel_von_tupel= ( (1,2), (3,5))
print(tupel_von_tupel, type(tupel_von_tupel))


# Zugriff wie bei einer Liste
print( obst_tupel[0])
print( obst_tupel[0:3])# ('Apfel', 'Banane', 'Kirsche')


# Tupel Unpacking
obst_1 = obst_tupel[0]
obst_2 = obst_tupel[1]
obst_3 = obst_tupel[2]
print(obst_1, obst_2, obst_3)


obst_1, obst_2, obst_3 = obst_tupel
print(obst_1, obst_2, obst_3)

obst_1, *obst = obst_tupel


print(obst_1, obst)

if "Banane" in obst_tupel: 
    print("Gefunden!") 

else:
    print('nicht vorhanden')



if "Banane" not in obst_tupel: 
    print('nicht vorhanden') 

else:
    print('Gefunden')    


# kein direct editing

obst_list = list( obst_tupel)
print(obst_tupel)
print(obst_list)

obst_list.append('Ananas')

print(obst_list)

# wandele die Liste in eine Tuper zurück
neue_obst_tupel = tuple(obst_list)
print(neue_obst_tupel )

