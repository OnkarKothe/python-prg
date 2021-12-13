# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:51:59 2021

@author: Onkar
"""
'''
You have x no. of 5 rupee coins and y no. of 1 rupee coins. 
You want to purchase an item for amount z. 
The shopkeeper wants you to provide exact change. 
You want to pay using minimum number of coins. 
How many 5 rupee coins and 1 rupee coins will you use? 
If exact change is not possible then display -1.

Input                                                                 # Output

Available Rs.1 __ coins Available Rs.5 __ notes  Amount to be made __ # Rs. 1 coins needed __ Rs. 5 notes needed

2                       4                           21                #        1                 4

11                      2                           11                #        1                 2

3                       3                           19                #        -1
'''
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    five = int(rupees_to_make/5)
    one_needed = rupees_to_make%5
    five_needed = five if five <= no_of_five else no_of_five
    if (five > no_of_five):
        one_needed = rupees_to_make - 5 * no_of_five     
    
    (print("No. of Five needed : {}\nNo. of One needed  : {}".format(five_needed,one_needed))) if one_needed <= no_of_one else (print(-1))   


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)