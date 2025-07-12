# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:02:01 2018

@author: joshu
"""
pieces = []
num=[1,1,2,2,2,8]
pieces = [int(i) for i in input().split()]
for i in range(0,6):
    print(num[i]-pieces[i] , end=' ')

