# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 17:49:12 2022

@author: Onkar
"""
'''
Write a Python function to rotate the list of elements by N positions. The function should return the rotated list.

Sample Input                                  Expected Output

Input list: [1, 2, 3, 4, 5, 6]
Number of positions to be rotated = 2          [5, 6, 1, 2, 3, 4]

Input list: [1, 2, 3, 4, 5, 6]
Number of positions to be rotated = 4          [3,4,5, 6, 1, 2]

Note : Assume that number of positions to be rotated is always a value >= 0 and <= length of the input list. 
'''

def rotate_list(input_list,n):
    if n>0 and n<=len(input_list):
        a=len(input_list)-n
        output_list=input_list[len(input_list) -n:] + input_list[:a]
        return output_list
    return False
input_list= [1,2,3]
output_list=rotate_list(input_list,3)
print(output_list)