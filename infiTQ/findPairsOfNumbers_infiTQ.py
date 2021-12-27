# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:02:21 2021

@author: Onkar
"""

#lex_auth_01269438594930278448
'''
Write a python function, find_pairs_of_numbers() which accepts a list of positive integers 
with no repetitions and returns count of pairs of numbers in the list that adds up to n. 
The function should return 0, if no such pairs are found in the list.
 

Sample Input                         Expected Output

[1, 2, 7, 4, 5, 6, 0, 3], 6          3

[3, 4, 1, 8, 5, 9, 0, 6], 9          4
'''

def find_pairs_of_numbers(num_list,n):
    c=0
    for i in num_list:
        for j in range(num_list.index(i)+1,len(num_list)):
          
            if (i+num_list[j])==n:
                #print(i,num_list[j])
                c+=1
    return c
    
num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))