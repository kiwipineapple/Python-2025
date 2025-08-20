# Liste erstellen 
obst = ["Apfel", "Banane", "Kirsche"]

obst.append("Orange")        # Am Ende hinzufügen 
print(obst)


obst.insert(1, "Mango")      # An Position 1 einfügen
print(obst)

obst.remove("Banane")        # Ein Element löschen

del obst[0]                  # Nach Index löschen
print(obst)

obst[0] = "Erdbeere" 
print(obst)

obst.clear()                 

