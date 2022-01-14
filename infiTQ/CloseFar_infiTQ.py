# -*- coding: utf-8 -*-,
"""
Created on Fri Jan 14 17:30:52 2022

@author: Onkar
"""
'''
Write a python function which accepts three numbers and returns True if

a. one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and

b. Number that is left out is "far", differing from both other values by 2 or more.

Return false if the above mentioned conditions are not satisfied.

Sample Input     Expected Output

4,1,3            True

5,6,7            False
'''

def close_number(num1,num2,num3):
    l=sorted(list([num1,num2,num3]))
    #print(l)
    if l[0]==l[1] or l[0]+1==l[1]:
        if l[1]+2 <= l[2]:
            return True
    elif l[1]==l[2] or l[1]+1==l[2]:
        if l[0]+2 <= l[1]:
            return True
    return False
    
print(close_number(6,9,6))