# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:34:23 2018

@author: joshu
"""

import math 

#this is your use input dont  for get to change

'''
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
'''

x1,y1 = 0, 0
x2,y2 = 1, 0
x3,y3 = 1, 1

print(x1,y1,x2,y2,x3,y3)

def dist(xi,xf,yi,yf):
    return math.sqrt((xf-xi)**2+(yf-yi)**2)

def theta(length1,length2):
    return math.atan2(length1,length2)*(180/math.pi)

def vectorize(A):
    xc = A*math.cos(math.pi/4)
    yc = A*math.sin(math.pi/4)
    return [xc,yc]

def slope(xi,xf,yi,yf):
    del_x = xf-xi
    del_y = yf-yi
    return (del_y/del_x)

def intersect(x0,y0,x00,y00,line1,line2):
    y1 = slope(line)*(xf-x0)+y0
    
    

d21 = dist(x1,x2,y1,y2)
d32 = dist(x2,x3,y2,y3)
d31 = dist(x1,x3,y1,y3)

print(d21,d32,d31)

if theta(d21,d32) == 45:
    print('yea1')
    dist = d31
else:
    print('no1')
    
if theta(d32,d31) == 45:
    print('yea2')
else:
    print('no2')
    
if theta(d31,d21) == 45:
    print('yea3')
else:
    print('no3')
    
print(vectorize(dist))    




   