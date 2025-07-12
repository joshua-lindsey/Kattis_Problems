# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:10:52 2018

@author: joshu
"""

from math import pi, sqrt

#r,h,p = map(int, input().split())
r,h,p = 10, 11, 0

rope =  pi* r + 2 * sqrt(r**2 + h**2)
percent = p / 100
knot = rope * percent

length = rope + knot
print(length)