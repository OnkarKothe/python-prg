# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 03:50:09 2021

@author: Onkar
"""
'''
In a given list, append every last number and find if its divisible by 10.
example:
input:
5
12 13 15 14 55
output:
23545
No

'''
n=int(input())
b=""
a=[]
data= [int(d) for d in input().split()]
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
