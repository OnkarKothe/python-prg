# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 08:46:09 2021

@author: Onkar
"""
'''
rotate prg
'''
l=[int(x)for x in input().split()]
it=int(input())
n=abs(it)%len(l)
print(n)
for i in range(n):
    if it>0:
        a=l.pop()
        l.insert(0,a)
    else:
        a=l.pop(0)
        l.append(a)
print(l)