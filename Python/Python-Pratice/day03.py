'''
DAY 3
'''

# Homework
# 1.
length = float(10)
unit = "inch"
if unit is "inch":
    print("%.3f inch = %.3f m" % (length, length*2.54))
elif unit is "m":
    print("%.3f m = %.3f inch" % (length, length/2.54))
else:
    print("Error input!")

# 2.
from random import randint
val = randint(1,6)
if val is 1:
    print("You got", val)
elif val is 2:
    print("You got", val)
elif val is 3:
    print("You got", val)
elif val is 4:
    print("You got", val)
elif val is 5:
    print("You got", val)
else:
    print("You got", val)

# 3.
val = randint(0,100)
if val >= 90:
    grade = 'A'
elif val >= 80 and val <90:
    grade = 'B'
elif val >= 70 and val <80:
    grade = 'C'
elif val >= 60 and val <70:
    grade = 'D'
else:
    grade = 'E'
print("Your score:", val)
print("You got", grade)

# 4.
import math
a = float(randint(1,100))
b = float(randint(1,100))
c = float(randint(1,100))
if a+b>c and a+c>b and b+c>a:
    print("a =", a, ", b =", b, ", c=", c)
    s = (a + b + c) / 2
    print("perimeter:", s)
    a = math.sqrt(s * (s - a) * (s - b)* (s - c))
    print("area:", a)
else:
    print("Failed")