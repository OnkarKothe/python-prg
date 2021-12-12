# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 12:11:00 2021

@author: Onkar
"""
'''
Given a string containing uppercase characters (A-Z), 
compress the string using Run Length encoding. 
Repetition of character has to be replaced by storing the length of that run.
Write a python function which performs the run length encoding for a given String 
and returns the run length encoded String.
Provide different String values and test your program

ip:
AAAABBBBCCCCCCCC
op:
4A4B8C

ip:
AABCCA
op:
2A1B2C1A
'''
def encode(message):
    l=list(message)
    num=l[0]
    count=1
    t=""
    if len(l)<=1:
        t=str(count)+num
    else:    
      for i in range(1,len(l)):
        if str(num)==str(l[i]):
            count+=1
        else:
            t+=str(count)+num
            num=l[i]
            count=1
      if l[len(l)-1]!=l[len(l)-2]:
            t+="1"+l[len(l)-1]
    return t
    
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)