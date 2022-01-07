# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:03:24 2022

@author: Onkar
"""
'''
Write a python function, nearest_palindrome() which accepts a number and returns 
the nearest palindrome greater than the given number. 

Sample Input      Expected Output

12300             12321

12331             12421

'''
def nearest_palindrome(number):
    number+=1
    while(True):
        if str(number)==str(number)[::-1]:
            return number
        number+=1

number=12300
print(nearest_palindrome(number))