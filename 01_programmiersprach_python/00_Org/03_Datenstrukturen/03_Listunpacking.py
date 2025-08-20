numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers)

first = numbers[0]
second = numbers[1]
third = numbers[2]

print(first, second, third)# 0 1 2

# ALternative
numbers2 = [5,6,7]
first2 , second2, third2 = numbers2
print(first2, second2, third2)#5 6 7


numbers = [0,1,2,3,4,5,6,7,8,9]
erstes, zweites, drittes, *others = numbers
print(erstes, zweites, drittes, others)
#0  1 2 [3, 4, 5, 6, 7, 8, 9]


erstes,*others, letztes = numbers
print(erstes, others,letztes)#0 [1, 2, 3, 4, 5, 6, 7, 8] 9

joshi,*bla, jenny = numbers
joshi, sofi, *bla, jenny = numbers  # 0 ,1 [2, 3, 4, 5, 6, 7, 8] 9
print(joshi, bla,jenny)#0 [1, 2, 3, 4, 5, 6, 7, 8] 9
















