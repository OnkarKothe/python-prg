# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:08:55 2021

@author: Onkar
"""
'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n]
 that do not appear in nums.
 
 Example :

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
'''
'''
n=list(map(int,input().split()))
op=[]
for i in range(1,len(n)+1):
    if i not in n:
        op.append(i)    
print(op)
'''
#using while loop
'''
i=list(map(int,input().split()))
op=[]
a=1
while a<=len(i):
    if a not in i:
        op.append(a)    
    a+=1
print(op)
'''
