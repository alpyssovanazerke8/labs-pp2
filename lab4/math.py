import math

#ex 1
n = int(input())
m = math.radians(n)

print(m)

#ex 2
height = float(input())
base1 = float(input())
base2 = float(input())

area = 0.5 * (base1 + base2) * height

print(area)

#ex 3
from math import tan, pi

n = int(input())
s = float(input())
area = n*(s**2)/(4*tan(pi/n))

print(area)

#ex 4
b = float(input())
h = float(input())
area = b * h
print(area)

