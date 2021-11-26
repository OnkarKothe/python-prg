# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:54:54 2021

@author: Onkar
"""
'''
Given an array of integer, perform k operations
so that the sum of element of final array is minimmum
example:
3
20 2 7 5
output:
15
'''
k=int(input())
n=[int(x)for x in input().split()]
for i in range(k):
    a=(max(n)//2)
    n.remove(max(n))
    n.append(a)
print(n)
print(sum(n))