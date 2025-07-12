# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:31:27 2018

@author: joshu
"""
import math

n, w, h = map(int, input().split())

m = math.sqrt(w**2 + h**2)
i = 0

while i < n:
    j = int(input())
    if j <= m:
        print('DA')
    else:
        print('NE')
    i+=1