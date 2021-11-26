# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:51:02 2021

@author: Onkar
"""
'''
input list form user
input a  space sequence string from list
example:
    [1,2,3,4,5]
    append 1
    insert 1 2
    pop 3
display list
'''
def val2(l,str1):
    str2=int(str1[1])
    if str1[0]=="append" or str1[0]=="a":
        l.append(str2)
    elif str1[0]=="pop" or str1[0]=="p":
        if int(str1[1])>=len(li):
            return "pop index out of range"
        else:       
            l.pop(str2)
    elif str1[0]=="remove" or str1[0]=="r":
        l.remove(str2)
    elif str1[0]=="insert" or str1[0]=="i":
        if len(str1)<3:
            str3=0
            l.insert(int(str3),str1[1])
        else:
            l.insert(int(str1[1]),int(str1[2]))
    return l

n=int(input("num of time: "))
b=[]
li=list(map(int,input("ent list: ").split()))
for i in range(n):
    a=list(input("::").split())
    b=(val2(li,a))
    #print(b)
print(b)        