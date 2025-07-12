# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:28:16 2018

@author: joshu
"""

import math 

h,v=map(int,input().split())
l=h/math.sin(v*math.pi/180)
print(math.ceil(l))
