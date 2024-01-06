# Write your solution here
from math import *

def hypotenuse(leg1: float, leg2: float):
    a = leg1**2
    b = leg2**2
    c = a + b
    return sqrt(c)
