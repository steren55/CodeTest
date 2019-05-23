'''
DAY 6
'''

import time
import math

flag = False
a = 1 if flag else 2
print(a)
print()

# Homework
# 1.
def gcd1(a, b):
    (a, b) = (b, a) if b > a else (a, b)
    while True:
        a %= b
        if a is 0: break
        b %= a
        if b is 0: break
    return a + b

def gcd2(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm1(a,b):
    return a * b // gcd1(a, b)


(a, b) = (3056874, 25968952)
print("(a, b) = (%d, %d)" % (a, b))
start = time.process_time()
GCD = gcd1(a, b)
end = time.process_time()
print("GCD:", GCD, "Time:", end - start, "s")
start = time.process_time()
GCD = gcd2(a, b)
end = time.process_time()
print("GCD:", GCD, "Time:", end - start, "s")
LCM = lcm1(a, b)
print("LCM:", LCM)
print()

# 2.
def is_palindrome(num):
    num = int(num)
    tmp = num
    sum = 0
    while tmp > 0:
        sum = sum * 10 + tmp % 10
        tmp //= 10
    return sum == num

for x in range(1, 101):
    if is_palindrome(x):
        print(x, end=" ")
print("is palindrome number")
print()

# 3.
def is_prime(num):
    num = int(num)
    fin = int(math.sqrt(num))
    for i in range(2, fin + 1):
        if num % i is 0:
            return False
    return True if num is not 1 else False

number = 121
if is_prime(number):
    print(number, "is prime number")
else:
    print(number, "is not prime number")
print()

# 4.
for x in range(1, 1001):
    if is_palindrome(x) and is_prime(x):
        print(x, end=" ")
print("is palindrome and prime number")
print()