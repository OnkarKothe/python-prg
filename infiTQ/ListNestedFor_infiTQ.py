# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:48:12 2022

@author: Onkar
"""
'''
Write a python function to generate and return the list of all possible 
sentences created from the given lists of Subject, Verb and Object.

Note: The sentence should contain only one subject, verb and object each.

Sample Input:                           

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

Expected Output:

I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
'''

def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    st1=''
    for a in subjects:
        for b in verbs:
            for c in objects:
                st1=a+" "+b+" "+c
                sentence_list.append(st1)

	
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))