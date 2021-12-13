# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:45:27 2021

@author: Onkar
"""

'''
Write a python function to check whether three given numbers can form the sides 
of a triangle. 
Hint
: Three numbers can be the sides of a triangle if none of the numbers are greater 
than or equal to the sum of the other two numbers
'''
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if (num1 + num2 <= num3) or (num1 + num3 <= num2) or (num2 + num3 <= num1):
        failure="Triangle can't be formed"
        return failure
    else:
        success="Triangle can be formed"
        return success
    #Write your logic here

    #Use the following messages to return the result wherever necessary
    return success
    return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)