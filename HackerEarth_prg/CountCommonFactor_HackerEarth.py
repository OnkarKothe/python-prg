# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:52:12 2021

@author: Onkar
"""
'''
This problem is asked in one of the HackerEarth contest.

Problem Statement: Little Robert likes mathematics. 
Today his teacher has given him two integers and asked to find out how many integers can divide both the numbers. 
Would you like to help him in completing his school assignment?

Input Formatting: 
Thre is two integers, a and b as input to the program.

Output Formatting: 
Print the number of common factors of a and b. 
Both the input value should be in a range of 1 to 10^12.

Example:

Input: 10 15
Output: 2
Explanation: The common factors of 10 and 15 are 1 and 5. 
So the answer will be 2.

'''
i,m=[int(x) for x in input().split()]
def grt(a,b):
    if a<b:
        return (a//2),b
    else:
        return (b//2),a
if i>0 and i<1000000000001 and m>1 and m<1000000000001:
    c=1
    mi=min(grt(i,m))
    print(mi)
    for x in range(2,mi+1):
        if i%x==0 and m%x==0:
            c+=1
print(c)            