# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:25:17 2018

@author: joshu
"""

a = int(input())
b = list(map(int, input().strip().split()))

c=[b[0]]
for i in range(a): 
    if b[i] == c[0]:
        pass
    elif b[i] > b[i-1]:
        c.append(b[i]) 
    else:
        pass
    
print(len(c))

for j in c:
    print(j, end=' ')