# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:43:47 2021

@author: Onkar
"""
'''
Write a python function, encrypt_sentence() 
which accepts a message and encrypts it based on rules given below and
 returns the encrypted message.

Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 
Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.

___________________________________________________________________________

Sample Input                          Expected Output

the sun rises in the east             eht snu sesir ni eht stea

'''
def encrypt_sentence(sentence):
    a=list(sentence.split())
    result=""
    for i in range(len(a)):
        if i%2==0:
            result+= a[i][::-1]+" "
        else:
               b=list(a[i])
               z=""
               for x in a[i]:
                   if x in ['a','e','i','o','u']:
                       b.append(x)
                       b.remove(x)
               for i in b:
                   z+=i
               result+=z+" "
    return (result.strip())
     
        

sentence="She sells sea shells on the sea"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
