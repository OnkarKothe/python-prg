# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 16:06:33 2022

@author: Onkar
"""
'''
Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.

A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y

For example, 123 is a seed of 738 as 123*1*2*3 = 738.

Sample Input   Expected Output

123,738        True

45,1000        False
'''

#lex_auth_0127135857243832321154

def seed_no(number,ref_no):
    a=list(str(number))
    for i in a:
        number*=int(i)
    if number==ref_no:
        return True
    return False
    
number=45
ref_no=1000
print(seed_no(number,ref_no))