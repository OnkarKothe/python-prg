# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 08:37:17 2021

@author: Onkar
"""

'''
problem of theif 
max num adjacent house

'''
n=[int(x) for x in input().split()]
e=[]
o=[]
even,odd=0,0
for i in range(len(n)):
    if n[i]%2==0:
        even+=n[i]
        e.append(i)
       # print(even)
    else:
        odd+=n[i]
        o.append(i)
        #print(odd)
if even > odd:
    print(even,"house number= ",e)
else:
    print(odd,"house number= ",o)

        