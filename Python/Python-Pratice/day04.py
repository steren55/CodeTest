'''
DAY 4
'''
for i in range(1, 10):
    for j in range(1, 10):
        print("%dx%d=%2d" % (j, i, i*j), end='\t')
    print()
print()

# Homework
# 1.
import math
number = int(131)
final = int(math.sqrt(number))
prime_flag = True
for i in range(2, final+1):
    if number % i is 0:
        prime_flag = False
        break
if prime_flag is True and number is not 1:
    print(number, "is prime number.")
else:
    print(number, "is not prime number.")
print()

# 2.
n1 = int(13)
n2 = int(39)
a = n1
b = n2
if b > a:
    a, b = b, a
while True:
    a %= b
    if a is 0: break
    b %= a
    if b is 0: break
gcd = a + b
lcm = n1 * n2 / gcd
print("(%d,%d) -> GCD: %d, LCM: %d" % (n1, n2, gcd, lcm))
print("(%d,%d) -> GCD: %d, LCM: %d" % (n1, n2, math.gcd(n1, n2), n1*n2/math.gcd(n1, n2)))
print()

# 3.
layer = int(5)
for i in range(0, layer):
    for j in range(0, i + 1):
        print("*", end = "")
    print()
print()

for i in range(0, layer):
    for j in range(0, layer - 1 - i):
        print(" ", end = "")
    for j in range(0, i + 1):
        print("*", end = "")
    print()
print()

for i in range(0, layer):
    for j in range(0, layer - 1 - i):
        print(" ", end = "")
    for j in range(0, i + 1):
        print("*", end = "")
    for j in range(0, i):
        print("*", end = "")
    print()
print()




for i in range(layer):
    for j in range(i + 1):
        print("*", end = "")
    print()
print()

for i in range(layer):
    for j in range(layer - 1 - i):
        print(" ", end = "")
    for j in range(i + 1):
        print("*", end = "")
    print()
print()

for i in range(layer):
    for j in range(layer - 1 - i):
        print(" ", end = "")
    for j in range(i + 1):
        print("*", end = "")
    for j in range(i):
        print("*", end = "")
    print()
print()