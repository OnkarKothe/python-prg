# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 03:50:09 2021

@author: Onkar
"""

n=int(input())
b=""
a=[]
data= [int(d) for d in input().split()]
print(data)
for i in range(n):
    c=str(data[i]%10)
    a.append(c)
    b+=(a[i])
e=int(b)
print(b)
if e%10==0:
    print("Yes") 
else:
    print("No")
