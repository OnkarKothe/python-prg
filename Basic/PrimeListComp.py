# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:05:22 2021

@author: Onkar
"""
'''
for n in range(100,200):
    if all(n%i!=0 for i in range(2,n)):
        print(n)
'''
n=int(input())
c=0
s=0
l=[i for i in range(2,n+1)if all(i%j!=0 for j in range(2,(int(i**0.5))+1))]
print(l)
s=l[0]
for i in range(len(l)):
    s+=l[i+1]
   # print(s)
    if s>n:
        break
    elif s in l:
      c+=1
print(c)