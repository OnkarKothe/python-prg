# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:53:46 2022

@author: Onkar
"""
'''
Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.

Otherwise, it should return false.

Sample Input           Expected Output

[1, 1, 2, 3, 1]        True

[1, 1, 2, 4, 3]        False
'''
def list123(nums):
    for i in range(len(nums)):
        if nums[i]==1 and i+1< len(nums):
            if nums[i+1]==2 and i+1< len(nums): 
                if nums[i+2]==3 and i+1 < len(nums):
                      return True
    return False
     

    

nums=[1, 2, 1, 2, 1]
print(list123(nums))   
