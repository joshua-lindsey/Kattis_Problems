# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:48:30 2018

@author: joshu
"""


num1, num2 = map(str,input().split())

X=num1[::-1]
Y=num2[::-1]

if X > Y:
    print(X)
else:
    print(Y)
    
  