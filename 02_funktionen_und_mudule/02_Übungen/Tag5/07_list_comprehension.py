# Ü1
# old_list = ["apfel", "banane", "kirsche", "dattel"]
# new_list = [obst.upper() for obst in old_list]
# print(new_list)

# Ü2
# import string
# old_string = ('a1b2c3d4')
# new_list = [int(zahl) for zahl in old_string if zahl in string.digits]
# print(new_list)

# Ü3
# import math
# quadrate_list = [int(math.pow(zahl, 2)) for zahl in range(11)]
# print(quadrate_list)

# ü4
wörter = ["Apfel", "Banane", "Kirsche", "Dattel"]
erst_buchstaben = [word[0] for word in wörter]
print(erst_buchstaben)



# Ü5
# new_list = [zahl for zahl in range(1, 101) if zahl % 3 == 0 and zahl % 5 == 0]
# print(new_list)

# Ü6
städte = ["Berlin", "München", "Hamburg", "Köln"]
städte.reverse()
print(städte)
neu_list = [city.upper() for city in städte]
print(neu_list)