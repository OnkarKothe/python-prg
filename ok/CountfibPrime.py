# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 09:38:16 2021

@author: Onkar
"""
a=int(input())
l=[]
c=0
for n in range(2,a+1):
    if all(n%i!=0 for i in range(2,n)):
        l.append(n)
for i in range(len(l)-2):
    if l[i]==(l[i-1]+l[i-2]):
        c+=1
print(c)