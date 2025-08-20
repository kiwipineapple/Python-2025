# List

# List von strings

buchstaben = ['a','b','c']
buchstaben2 = ["a","b","c"]

print(buchstaben, type(buchstaben))# ['a', 'b', 'c'] <class 'list'>

# Liste von Zaheln
numbers = [1,2,3,4,4,5,6,0,8,9,5]
print(numbers, type(numbers))

# Matrix

matrix =[ [3 , 4 ], [1 , 2]]
print(matrix, type(matrix))

# List von Nullen
zeros = [0]*30
print(zeros)
# combine two lists together
combined = buchstaben2 + numbers
print(combined)
# conversion in einer Liste
numbersrange = range(20)
print(numbersrange)

numbersrange = list(numbersrange)
print(numbersrange)# 

