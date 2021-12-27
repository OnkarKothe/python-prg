# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:01:07 2021

@author: Onkar
"""

'''
Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
145 is a Strong number as 1! + 4! + 5! = 145. 

Sample Input                         Expected Output

num_list = [145,375,0,100,2]         [145, 2]
'''
def factorial(number):
       return 1 if (number == 1 or number == 0) else number * factorial(number - 1)

def find_strong_numbers(num_list):
    l=[]
    
    for i in num_list:
        a=str(i)
        fact=[]
        b=[int(x)for x in a]
        for j in b:
            
            fact.append(factorial(j))
     
        if sum(fact)==i:
            l.append(i)
    return l    

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)