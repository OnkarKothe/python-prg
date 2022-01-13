#lex_auth_0127136251125350401190

"""
Created on Thu Jan 13 15:27:29 2022

@author: Onkar
"""
'''
Write a python function to find out whether a number is divisible by the sum of its digits. 
If so return True,else return False.

Sample Input   Expected Output

42             True

66             False
'''
def divisible_by_sum(number):
    l=list(str(number))
    s=0
    for i in l:
        s+=int(i)
    if number%s==0:
        return True
    return False
    

    
number=42
print(divisible_by_sum(number))