import random
# Ü1
# num1 = random.random()
# num2 = random.random()
# num3 = random.random()
# num_list = [num1, num2, num3]
# print(num_list)

# Ü2
# for i in range(5):
#     print(random.randint(1,6))

# Ü3
# for i in range(3):
#     print(random.uniform(1.5, 3.5))

# Ü4
# color = ['red', 'yellow', 'blue']
# print(random.sample(color,3))

# # Ü5
# random.seed(123)
# print(random.randint(1, 100))


# Ü6
# zahlen = [10, 20, 30, 40]
# random.shuffle(zahlen)
# print(zahlen)

# Ü7
# obst = ["Apfel", "Banane", "Kirsche", "Orange"]
# print(random.sample(obst, 2))

# Ü8
# a = 0
# b = 0
# c = 0
# d = 0
# e = 0
# f = 0
# for i in range(100):
#     zahl = random.randint(1, 6)
#     if zahl == 1:
#         a += 1
#     elif zahl == 2:
#         b += 1
#     elif zahl == 3:
#         c += 1
#     elif zahl == 4:
#         d += 1
#     elif zahl == 5:
#         e += 1
#     elif zahl == 6:
#         f += 1
# print(f'1 wurde {a}-mal geworfen')
# print(f'2 wurde {b}-mal geworfen')
# print(f'3 wurde {c}-mal geworfen')
# print(f'4 wurde {d}-mal geworfen')
# print(f'5 wurde {e}-mal geworfen')
# print(f'6 wurde {f}-mal geworfen')

# Ü9
import string
zeichen = string.ascii_letters + string.digits
password = random.sample(zeichen, 8)
delimiter = ''
join_str = delimiter.join(password)
print(join_str)