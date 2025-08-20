list1 = [1, 2, 3]
list2 = [10, 20]
list3 = [100, 200, 300, 400]

# Using map() with lists of different lengths
result = map(lambda x, y, z: x + y + z, list1, list2, list3)
# Shortest List: The process stops when the shortest list is exhausted.

print(list(result))  # Output: [111, 222]
