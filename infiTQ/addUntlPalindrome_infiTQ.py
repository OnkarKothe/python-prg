# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:25:37 2021

@author: Onkar
"""
'''

'''
'''
def pal(st):
     if st==(st[::-1]):
           print(st[::-1])
    
     else:
           add(st)
def add(st1):
        result=0
        result=int(st1)+int(st1[::-1])
        pal(str(result))
    
st=input()
pal(st)
   
   '''
   #or
   
'''
pt=int(input())
while True:
    pt=str(pt)
    ct=pt[::-1]
    nt=int(pt)+int(ct)
    if str(nt)==str(nt)[::-1]:
        break
    pt=nt
print(nt)
'''