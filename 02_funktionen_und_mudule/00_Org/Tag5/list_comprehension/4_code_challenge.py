original_list = ["Dog", 10, 11.5, 12.5, 15, 16, 19, 20, "Cat"]

bow_meaw_list = [str(x) + " bow bow" if x % 2 == 0 else str(x) + " meaw"
                 for x in original_list if (isinstance(x, int) and x <= 19)]

print(bow_meaw_list)


