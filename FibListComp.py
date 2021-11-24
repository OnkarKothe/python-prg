# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:35:11 2021

@author: Onkar
"""

def fib(n):
    return n if n<=1 else (fib(n-1)+fib(n-2))
num=[1,2,3,4,5,6]
print([fib(x) for x in num])

'''
l=[y for x in num if (y:=fib(x)%2==0)]
print(l)
'''