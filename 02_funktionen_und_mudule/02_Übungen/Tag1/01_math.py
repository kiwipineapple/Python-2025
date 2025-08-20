import math

print(round(math.pi, 5))
print(round(math.e, 5))

print(math.sqrt(49))

a = 2 ** 8
b = math.pow(2,8)
print(type(a), type(b))

print(math.floor(3.7))
print(math.floor(2.4))
print(math.ceil(3.7))
print(math.ceil(2.4))

print(math.sin(math.radians(90)))

print(math.fabs(-5))
print(abs(-5))

umfang = 2 * math.pi * 7
print(umfang)

print(math.log(100, 10))

print(round(math.pi, 6))

for i in range(1, 11):
    print(round(math.sqrt(i), 2))