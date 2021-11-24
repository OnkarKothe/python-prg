# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:06:51 2021

@author: Onkar
"""
'''
Given the arrival and departure times of all trains that reach a railway station, 
the task is to find the minimum number of platforms required for the railway station so that no train waits. 
We are given two arrays that represent the arrival and departure times of trains that stop.

Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00} 
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
Output: 3 
Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)

Input: arr[] = {9:00, 9:40} 
dep[] = {9:10, 12:00} 
Output: 1 
Explanation: Only one platform is needed. 
'''
def numplat(at,dt):
    
    at.sort()
    dt.sort()
    n=len(at)
    i,j=1,0
    platneed=1
    result=1
    while i<n and j<n:
        if at[i] <= dt[j]:
            platneed+=1
            i+=1
        elif at[i] > dt[j]:
            platneed-=1
            j+=1
        if platneed > result:
            result=platneed
            
    return result      

arr=list(map(int,input().split(",")))
dep=list(map(int,input().split(",")))
a=numplat(arr,dep)
print(a)