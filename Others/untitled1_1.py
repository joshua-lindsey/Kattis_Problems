# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:11:50 2018

@author: joshu
"""

A = 22

def del_x(Vo,t):
    return(Vo*t + 0.5*(A)*(t)**2)
    
def Vx(Vox, t):
    return(Vox + A*t)
   
b1 = 0
b2 = 2
b3 = 4 
b4 = 6
b5 = 8 

B1 = 0
B2 = 0
B3 = 0
B4 = 0
B5 = 0

bv1 = 0

for t in range(0,10):
    while bv1 < 55:
        bx1 = del_x()
        
        