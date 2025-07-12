# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:51:11 2018

@author: joshu
"""
import math

a = [int(i) for i in input().split('/')]
print(a)

def dec(f):
    fn = f[0]
    fd = f[1]
    gcd = math.gcd(fn,fd)
    print(fn, fd)
    print(gcd)
    if fd == 1:
        blah = fn - 32
        return (fn - 32) * (5/9)
    else:
        pass
    
print(dec(a))  
'''
A = a[0] / a[1]
decimal = nume(A)
print(decimal)

if decimal == 0:
    print('0/1')
else:
    
    print(decimal)
'''