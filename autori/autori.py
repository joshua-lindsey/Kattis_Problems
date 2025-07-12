# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:48:32 2018

@author: joshu
"""

A = input()
a = A.split("-")
for i in range(len(a)):
    print(a[i][0].upper(), end='')

