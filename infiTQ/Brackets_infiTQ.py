# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:23:10 2022

@author: Onkar
"""
'''
Write a python function which accepts a string containing a pattern of brackets and 
returns true if the pattern of brackets is correct. Otherwise it returns false.

The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.

Sample Input        Expected Output

)()((()())          False

()((())())          True
'''
def bracket_pattern(input_str):
    input_str=list(input_str)
    if input_str[0]=="(":
         if input_str[len(input_str)-1]==")":
             if input_str.count("(")- input_str.count(")")==0:
                 return True
    return False
     

    
input_str="(())"
print(bracket_pattern(input_str))