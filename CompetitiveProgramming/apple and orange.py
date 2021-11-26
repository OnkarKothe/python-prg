# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 08:35:18 2021

@author: Onkar
"""
l=list(map(int,input().split()))
a=int(input())
li=list(map(int,input().split()))
b=int(input())
s=li[0]
t=li[1]
ca=0
co=0
if l[0]>0:
 for i in range(1,l[0]+1):
    d=int(input())
    if (a+d)>=s and (a+b)<=t:
        ca+=1
 print("apple",ca)
if l[1]>0:
 for i in range(1,l[1]+1):
    d1=int(input())
    if (b-d1)>=s and (b-d1)<=t:
        co+=1
 print("or",co)