# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:26:22 2018

@author: joshu
"""

from datetime import timedelta

Ct = [int(i) for i in input().split(':')]
Bt = [int(i) for i in input().split(':')]

c = Ct[0]*60*60 + Ct[1]*60 + Ct[2]
b = Bt[0]*60*60 + Bt[1]*60 + Bt[2]

if b == c:
    t = '24:00:00'
if b > c:
    sec = b - c
    t = str(timedelta(seconds = sec))
if b < c:
    sec = 24*60**2 - c + b
    t = str(timedelta(seconds = sec))

if len(t) == 7:
    t = '0' + t
    
print(t)