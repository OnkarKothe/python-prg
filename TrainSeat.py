# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:18:35 2021

@author: Onkar
"""
'''
Theirs a program of train.
Total number of seat are from 1 to 120
User will enter any seat number
Output should be displayed the opposite of its seat number and as well as it's type

Example:
Input: 6
Output: 7 ws

Input:1
Output:12 ws

Explanation:
Seat arrangement in train
1    2    3  4 5 6
12 11 10 9 8 7

1, 6, 7, 12 are window seat
2,5,8,11 middle seat
3,4,9,10 are last seat
'''
i=1
print("ent seat num 1:120 ")
while i==1:
 loc=int(input(":"))
 if loc>0 and loc<121:
     l=[x for x in range(-5,7)]
     for i in range(6,120,12):
         if (loc-i) in l:
             a=loc-i
             if a<=0:
                 op=loc+(abs(a*2)+1)
             else:
                 op=loc-((a*2)-1)  
             if a==-5 or a==0 or a==6 or a==12:
                 print(op,"ws")
             elif a==-4 or a==-1 or a==2 or a==5:
                 print(op,"ms")
             else:
                print(op,"ls")
 i=int(input("1:0 ::"))
 
 
