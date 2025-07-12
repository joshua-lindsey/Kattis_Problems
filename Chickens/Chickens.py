# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:16:16 2018

@author: joshu
"""

p,c = map(int,input().split())

if p>c:
    d=p-c
    if d==1:
        print('Dr. Chaz needs {} more piece of chicken!'.format(d))
    else:
        print('Dr. Chaz needs {} more pieces of chicken!'.format(d))
        
elif c>p:
    d=c-p
    if d==1:
        print('Dr. Chaz will have {} piece of chicken left over!'.format(d))
    else:
        print('Dr. Chaz will have {} pieces of chicken left over!'.format(d))
        
else:
    pass
    
