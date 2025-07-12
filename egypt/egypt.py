# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 13:26:57 2018

@author: joshu
"""
 
while True:
    num1, num2, num3 = map(int,input().split())
    pyth= [num1,num2,num3]
    pyth.sort()
    
    if pyth[0] == 0 and pyth[1] == 0 and pyth[2] == 0:
        break
    elif pyth[0]**2 + pyth[1]**2 == pyth[2]**2: 
        print('right')
    else:
        print('wrong')