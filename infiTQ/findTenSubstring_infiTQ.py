# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:15:45 2022

@author: Onkar
"""
'''
A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

Handle the possible errors in the code written inside the function.

Sample Input

Expected Output

'3523014'

['5230', '23014', '523', '352']
'''
#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    a=list(num_str)
    l=int(a[0])
    li=''
    final=[]
    for j in range(len(a)):
      l=0
      li=''
      for i in range(j,len(a)):
        l+=int(a[i])
        li+=a[i]
        print(l)
        if l==10:
            final.append("".join(li))
            #break
        elif l>10:
            break
    return final

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)