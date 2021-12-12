# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:30:32 2021

@author: Onkar
"""
'''
Write a python program that displays a message as follows for a given number:

If it is a multiple of three, display "Zip"
If it is a multiple of five, display "Zap".
If it is a multiple of both three and five, display "Zoom".
If it does not satisfy any of the above given conditions, display "Invalid".

'''
def display(num):
    message=""
    #write your logic here
    if num%3==0 and num%5==0:
        message="zoom"
    elif num%3==0:
        message= "Zip"
    elif num%5==0:
        message="Zap"
    else:
        message='Invalid'
    
    return message

#Provide different values for num and test your program
message=display(9)
print(message)