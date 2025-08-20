def infos(name, stadt):
    print(f"{name} lebt in {stadt}")

daten_liste = ["Anna", "Berlin"]
infos(*daten_liste)     # entspricht: infos("Anna", "Berlin")


print(*daten_liste)