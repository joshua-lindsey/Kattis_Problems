# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:41:57 2018

@author: joshu
"""
import math
'''
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
d = [a,b,c]
'''
row1 = [6,1,9]
row2 = [5,2,8]
row3 = [4,3,7]

def find(i): 
    if i < 10:
        r = row1.index(i)
    else:
        r = 0
    return r


def find_row(i):
    if i > 9:
        r = 0
    if i in row1:
        r = 1
    elif i in row2:
        r = 2
    elif i in row3:
        r = 3

    return(r)
    
def length(N,M):
    n = int(N)
    m=int(M)
    if n == m:
        d = 1
    elif abs(n-m) == 1:
        d= math.sqrt(2)
    elif abs(n-m) == 2:
        d= 2*math.sqrt(2)
    else:
        d=4
    return d
    
i = 1
d = 0
while i < 10:
    a = find_row(i)
    b = find_row(i+1)

    c = length(a,b)
    d +=c
    print(c,d)
    i += 1  