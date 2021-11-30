# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:44:35 2021

@author: Onkar
"""

'''
 There are N horses in the stable. The skill of the horse i is represented by an integer S[i].
 The Chef needs to pick 2 horses for the race such that the difference in their skills is minimum.
 This way, he would be able to host a very interesting race.
 Your task is to help him do this and
 report the minimum difference that is possible between 2 horses in the race.

 Input:
 First line of the input file contains a single integer T, the number of test cases.
 Every test case starts with a line containing the integer N.
 The next line contains N space separated integers where the i-th integer is S[i].

 Output:
 For each test case, 
 output a single line containing the minimum difference that is possible.

 Constraints:
 1 ≤ T ≤ 10
 2 ≤ N ≤ 5000
 1 ≤ S[i] ≤ 1000000000

 Example:

 Input:
 1
 5
 4 9 1 32 13

 Output:
 3
'''
t=int(input())
while t>0:
    t-=1
    num=int(input())
    n=[int(x)for x in input().split()]
    if num==len(n):
        n.sort()
        mid=n[1]-n[0]
        for i in range(0,num-1):
            mid1=n[i+1]-n[i]
            if mid > mid1:
                mid=mid1
    print(mid)
    