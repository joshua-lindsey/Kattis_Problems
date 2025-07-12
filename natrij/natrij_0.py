# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 11:10:24 2018

@author: joshu
"""

ct = input()
bt = input()

Ct = list(map(int,  ct.split(':')  ))
Bt = list(map(int,  bt.split(':')  ))
#####################################################
if Ct == Bt:
    print('24:00:00')
else:
    if Bt[2] == Ct[2]:
        C=0
        c= Bt[2] - Ct[2]
    elif Bt[2] > Ct[2]:
        C=0
        c= Bt[2] - Ct[2]
    else:
        C=1
        c = 60 - Ct[2] + Bt[2]
        if c == 60:
            c = 0
    
    if Bt[1] ==  Ct[1]:
        B = 0
        b = Bt[1] - Ct[1] - C
    elif Bt[1] > Ct[1]:
        B = 0
        b = Bt[1] - Ct[1] - C
    else:
        B = 1
        b = 60 - Ct[1] + Bt[1] - C
        if b == 60:
            b=0
        
    if Bt[0] == Ct[0]:
        a = Bt[0] - Ct[0] - B
    elif Bt[0] > Ct[0]:
        a = Bt[0] - Ct[0] - B
    else:
        a = 24 - Ct[0] + Bt[0] - B
        if a == 24:
            a = 0

    out1 = [a,b,c]
    out = list(map(str,  out1))
    
    
    for i in range(len(out)):
        if len(out[i]) ==1:
            out[i] = '0'+ out[i]
    
    output = ':'.join(x for x in out)
    print(output)

