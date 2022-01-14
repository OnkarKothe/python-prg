# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:36:21 2022

@author: Onkar
"""
'''
Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.

Sample Input      Expected Output

14 and 35           7

800 and 2800       400
'''
def find_gcd(num1,num2):
    a,b=mxmin(num1,num2)
    if a%b==0:
        return a
    else:
       for i in range((a//2)+1,0,-1):
          if b%i==0 and a%i==0:
              return i
    
def mxmin(num1,num2):
    if num1<num2:
        return num1,num2
    return num2,num1

num1=14
num2=35
print(find_gcd(num1,num2))