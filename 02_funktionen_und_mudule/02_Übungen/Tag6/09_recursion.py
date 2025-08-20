# Ü1
def summe(n):
    sum = 0
    if n > 0:
        sum = n + summe(n-1)
    return sum

print(summe(6))