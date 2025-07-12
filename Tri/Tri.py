# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 16:09:45 2018

@author: joshu
"""

a,b,c = map(int,input().split())

if b*c == a:
    print('{a}{op1}{b}{op2}{c}'.format(a=a,b=b,c=c,op1="=",op2='*'))
elif b/c == a:
    print('{a}{op1}{b}{op2}{c}'.format(a=a,b=b,c=c,op1="=",op2='/'))
elif b+c == a:
    print('{a}{op1}{b}{op2}{c}'.format(a=a,b=b,c=c,op1="=",op2='+'))
elif b-c == a:
    print('{a}{op1}{b}{op2}{c}'.format(a=a,b=b,c=c,op1="=",op2='-'))
elif a+b == c:
    print('{a}{op1}{b}{op2}{c}'.format(a=a,b=b,c=c,op1="+",op2='='))
elif a-b == c:
    print('{a}{op1}{b}{op2}{c}'.format(a=a,b=b,c=c,op1="-",op2='='))
elif a*b == c:
    print('{a}{op1}{b}{op2}{c}'.format(a=a,b=b,c=c,op1="*",op2='='))
else:
    print('{a}{op1}{b}{op2}{c}'.format(a=a,b=b,c=c,op1="/",op2='='))
    