# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:32:46 2021

@author: Onkar
"""
'''
FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.

A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate.

Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.

Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. 

The delivery charges are as mentioned below:
    

Distance in kms   Delivery charge in Rs per km

For first 3kms     0

For next 3kms      3

For the remaining  6


Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point, 

write a python program to calculate the final bill amount to be paid by a customer. 

The below information must be used to check the validity of the data provided by the customer: 

Type of food must be āVā for vegetarian and āNā for non-vegetarian.

Distance in kms must be greater than 0.

Quantity ordered should be minimum 1.

If any of the input is invalid, the bill amount should be considered as -1.

'''
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    d=0
    if distance_in_kms>0 and quantity_ordered>0 and (food_type=="N" or food_type=="V"):
        if food_type=="V":
           bill_amount=quantity_ordered*120
        elif food_type=="N":
            bill_amount=quantity_ordered*150
        distance_in_kms-=3 
        if distance_in_kms<=3 and distance_in_kms>0:
            d=3*distance_in_kms
        elif distance_in_kms>3:
            d+=3*3
            distance_in_kms-=3 
            d+=distance_in_kms*6 
    else:
        bill_amount=-1
    #write your logic here
    return (bill_amount+d)

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,8)
print(bill_amount)