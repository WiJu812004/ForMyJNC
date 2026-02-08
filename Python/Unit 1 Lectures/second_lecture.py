m = max(7.5, 9.5, 11.0, 6.9, 5.4)
print(m)

print('---------------')
n = max(min(9.5, 11.0), 6.9, 5.4)
print(n)

print('---------------')
import math
print(math.pi)
print(math.cos(math.pi/4))

print('---------------')
from math import pi, cos
print(pi)
print(cos(0.25*pi))

print('---------------')
from math import *
print(pi)
print(cos(0.25*pi))

print('---------------')
def average3(x, y, z):
    """Returns average of 3 integers"""
    tot = x + y + z
    return tot / 3.0

a = 15
b = 30
c = 45

d = average3(a, b, c)
print(d)

print('---------------')
def average3(x, y, z):
    """Returns average of 3 integers"""
    x = x + y + z
    return x / 3.0

a = 15
b = 30
c = 45

d = average3(a, b, c)
print(d)

print('---------------')
def average3(x, y, z):
    """Returns average of 3 integers"""
    tot = x + y + z
    return tot / 3.0

a = 15
b = 30
c = 45

tot = average3(a, b, c)
print(tot)

print('---------------')
def div_add(n1, n2, n3):
    """Divide n1 by n2, then add n3"""
    return n1 / n2 + n3

a = 7
b = 1
c = 35

print(div_add(n2 = 7, n3 = 1, n1 = 35))

print('---------------')
def calc_vol(length, width, height = 1):
    """Calculate the volume of a rectangular prism"""
    vol = length*width*height
    return vol

print(calc_vol(2, 3),'cubic units')
print(calc_vol(2, 3, 2),'cubic units')

print('---------------')
