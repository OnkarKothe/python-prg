# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:58:05 2022

@author: Onkar
"""
'''
Write a python function, remove_duplicates() which accepts a string and removes 
all duplicate characters from the given string and return it.

Sample Input                        Expected Output

1122334455ababzzz@@@123#*#*         12345abz@#*
'''
def remove_duplicates(value):
    l=[]
    for i in value:
        if i not in l:
            l.append(i)
    return "".join(l)
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))