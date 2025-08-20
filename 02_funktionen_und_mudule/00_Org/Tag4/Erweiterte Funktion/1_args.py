def summieren(*zahlen):
    print(zahlen)
    return sum(zahlen)

print(summieren(1, 2, 3))        # Ausgabe: 6
print(summieren(10, 20, 30, 40)) # Ausgabe: 100



"""
def summe(*args):
    print(type(args))
    return sum(args)


print(summe(1, 2, 3))

# [1,2,3] List Comprehension

# print(   sum((4,5))    )


"""

