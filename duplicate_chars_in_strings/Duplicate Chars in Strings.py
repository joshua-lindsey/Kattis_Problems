# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:05:29 2018

@author: joshu
"""

inn = str(input())

In=list(inn)
In.insert(0,0)
Out=[]

for i in range(len(In)):
    if In[i] == In[i-1]:

        continue
    else:
        Out.append(In[i])
Out.pop(0)        
for i in Out:
    print(i, end= '')