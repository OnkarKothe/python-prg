# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:16:53 2021

@author: Onkar
"""
'''
Find the min number of coin required to from any value bet 1 to n both inclivesive
-coins are 1,2 and 5 
'''
i=1
while i==1:
 n=int(input())
 if n<=3:
     if n==1:
      print("1")
     else:
      print("2")   
 else:
     c1,c2=0,0
     c5=(n-4)//5
     b=n-(c5*5)
     if b%2==0:
         c1=2
     else:
         c1=1
     b-=c1
     c2=b//2
     print(c1+c2+c5)
 i=int(input(":::"))
