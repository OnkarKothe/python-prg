# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 20:11:02 2021

@author: Onkar
"""
'''
Write a recursive function, is_palindrome() to find out whether a string is a
 palindrome or not. The function should return true, if it is a palindrome.
 Else it should return false. 

Note- Perform case insensitive operations wherever necessary.
'''
#lex_auth_01269442114344550475

def is_palindrome(word):
    return True if word.upper()==(word.upper())[::-1] else False

#Provide different values for word and test your program
result=is_palindrome("MadAM")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")