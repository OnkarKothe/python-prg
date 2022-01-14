# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:24:32 2022

@author: Onkar
"""
'''
Given a list of integers and a number. Write a python function to find and return the sum of the elements of the list. 
Note: Don't add the given number and also the numbers present before and after the given number in the list.

Sample input                              Expected output

list=[1,2,3,4], number=2                  4

list=[1,2,2,3,5,4,2,2,1,2],number=2       5

list=[1,7,3,4,1,7,10,5],number=7          9

list=[1,2,1,2],number=2                   0
'''
def sum_of_elements(num_list,number):
    result_sum=0
    for i in range(len(num_list)):
        if num_list[i] !=number:
            if i==0:
                if num_list[i+1]!=number:
                    result_sum+=num_list[i]
            elif i==len(num_list)-1:
                if num_list[i-1]!=number:
                    result_sum+=num_list[i]
            elif i>0 and i<len(num_list)-1:
                if num_list[i-1]!=number and num_list[i+1]!=number:
                    result_sum+=num_list[i]
                
        
    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))