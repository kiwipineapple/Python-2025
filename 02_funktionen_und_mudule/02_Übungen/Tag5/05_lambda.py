# # Übung 1
# y = lambda x: x**2
# print(y(7))

# Ü2
# my_list = [('Anna', 25), ('Bernd', 32), ('Clara', 28), ('David', 21)]
# # sorted_list = my_list.sort(key= lambda x: x[1])
# sorted_list = sorted(my_list, key= lambda x: x[1])
# print(sorted_list)

# Ü3
# name_list = ['Sophie', 'Anna', 'Maximilian', 'Ben', 'Charlotte']
# sorted_name_list = sorted(name_list, key=len)
# print(sorted_name_list)

# Ü4
zahlen_list = [42, 17, 23, 56, 34]
sorted_zahlen_list = sorted(zahlen_list)
print(sorted_zahlen_list)

reverse_sorted_zahlen_list = sorted(zahlen_list, reverse=True)
print(reverse_sorted_zahlen_list)