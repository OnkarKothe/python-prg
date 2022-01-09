# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:42:04 2022

@author: Onkar
"""

'''
Given a list of numbers, write a python function which returns 
true if one of the first 4 elements in the list is 9. 
Otherwise it should return false.

The length of the list can be less than 4 also.

Sample Input         Expected Output

[1, 2, 9, 3, 4]      True

[1, 2, 9]            True

[1, 2,3,4]           False
'''

def find_nine(nums):
    if 9 in nums[0:4]:
        return True
    return False
    

nums=[1,0,4,9,6,9]
print(find_nine(nums))