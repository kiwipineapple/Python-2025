def infos(name, stadt):
    print(name)
    print(f"{name} lebt in {stadt}")

daten_dict = {"name": "Tom", "stadt": "Hamburg"}
infos(**daten_dict)     # entspricht: infos(name="Tom", stadt="Hamburg")

# print(**daten_dict) # Error
# **dict darf nur beim Funktionsaufruf verwendet werden – niemals als Argument für print()
#  oder als eigenständiger Ausdruck.