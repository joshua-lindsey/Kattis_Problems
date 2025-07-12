# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:41:30 2018

@author: joshu
"""
     
num1 = input()
num2 = input()

len1 = len(num1)
len2 = len(num2)

len_n = abs(len1 - len2)

if len1 > len2:
    num2 = '0' * len_n + num2
else:
    num1 = '0' * len_n + num1



new1 = ''
new2 = ''

for i in range(len(num1)):
    if i > len(num2):
        break
    if num1[i] > num2[i]:
        new1 += num1[i]
    elif num1[i] < num2[i]:
        new2 += num2[i]
    else:
        new1 += num1[i]
        new2 += num2[i]

print(int(new1) if len(new1) else 'YODA')
print(int(new2) if len(new2) else 'YODA')
