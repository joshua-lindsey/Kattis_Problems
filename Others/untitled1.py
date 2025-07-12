# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:44:25 2018

@author: joshu
"""

a = int(input())
b = list(map(int, input().strip().split()))

c=[]
for i in range(a): 
    if b[i] > b[i-1]:
        c.append(b[i]) 
    else:
        pass
    
print(len(c))


for j in c:
    print(j, end=' ')