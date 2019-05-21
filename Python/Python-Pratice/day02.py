'''
DAY 2
'''
a = 2
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# c = int(input('c = '))
# d = int(input('d = '))
# print('%d^%d = %d' % (c,d,c**d))

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 =", flag1)
print("flag2 =", flag2)
print("flag3 =", flag3)
print("flag4 =", flag4)
print("flag5 =", flag5)
print(flag1 is True)
print(flag2 is not False)

f1 = 3 is 2
f2 = 3 == 2
print("f1 =", f1, ',f2 =', f2)

x = y = [1,2,3]
z = [1,2,3]
f1 = x is y
f2 = x is z
f3 = x == y
f4 = x == z
print("f1 =", f1, ',f2 =', f2)
print("f3 =", f3, ',f4 =', f4)
print("id(x) =", id(x))
print("id(y) =", id(y))
print("id(z) =", id(z))
print()

# Homework
# 1.
C = float(30)
F = 1.8*C + 32.0
print("C =", C, "=> F =", F)
F = float(70)
C = (F-32.0) / 1.8
print("F = %.1f => C = %.1f" % (F, C))
print()

# 2.
import math
r = 10
p = 2*math.pi*r
a = math.pi*r*r
print("radius:", r)
print("perimeter: %.3f" % (p))
print("area: %.3f" % (a))
print()

# 3.
y = 2015
leep = (y % 4 ==0 and y % 100 != 0) or (y % 400 == 0 and y % 3200 != 0)
print(y, "is leep year:" ,leep)