# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:41:08 2022

@author: Onkar
"""
'''
Write a python function which accepts a sentence and returns a list in which 
first value is the count of upper case letters and second value is the count of lower case 
letters in the sentence. Ignore spaces, numbers and other special characters if any.

Sample input         Expected Output

Hello world!         [1,9]

Welcome to Mysore    [2,13]
'''
def find_upper_and_lower(sentence):
    result_list=0
    cntup=0
    cntlow=0
    for i in sentence:
        if i.isupper():
            cntup+=1
        elif i.islower():
            cntlow+=1
    result_list=([cntup,cntlow])
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))