cities = ["Bremen", "Hamburg", "Berlin", "Duisburg"]

#hallo_city = [  "Hallo " + city    for city in cities    if len(city) <= 6  ]
#print(hallo_city)



my_list = [  x    for x in range(1,10)   if x<5   ]
print(my_list)


# Das obige List Comprehension ist eine kürzere Version des folgenden Codes,
# der eine for-Schleife und eine if-Bedingung verwendet
"""
meaw_city = []

for city in cities:
    if len(city) <= 6:
        meaw_city.append("Hallo "+city)


print(meaw_city)
"""
