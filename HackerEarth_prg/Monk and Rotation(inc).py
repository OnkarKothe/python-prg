# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:12:52 2021

@author: Onkar
"""
'''
num of time rotate
'''
t=int(input())
e=[]
while (t>0):
  t-=1
  z=list(map(int,input().split()))
  l=[int(x)for x in input().split()]
  n=abs(z[1])%z[0]
  for i in range(abs(z[1])):
    if z[1]>0:
        a=l.pop()
        l.insert(0,a)
    else:
        a=l.pop(0)
        l.append(a)
  for i in range(len(l)):
    print(l[i],end=" ")  