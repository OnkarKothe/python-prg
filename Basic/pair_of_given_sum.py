# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 13:15:03 2021

@author: Onkar
"""

n=[int(x) for x in input().split()]
t=len(n)
target=int(input("target: "))
for i in range(t):
    if n[i]+(n-n[i])==target:
        print(n[i],n[i+1])
