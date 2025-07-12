# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:08:03 2018

@author: joshu
"""

x = input()
X=list(x)
pos = [0,1,2,3]
 
def A(a):
    a[1], a[2] = a[2], a[1]
    return a
def C(c):    
    c[1], c[3] = c[3], c[1]
    return c
def B(b):
    b[2], b[3] = b[3], b[2]
    return b

for i in X:
    if i == 'A':
        A(pos)
    elif i == 'B':
        B(pos)
    elif i == 'C':
        C(pos)
    else:
        pass

        
print(pos.index(1))            