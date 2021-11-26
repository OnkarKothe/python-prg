# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:03:16 2021

@author: Onkar
"""
'''

example:
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''

def oper(l,str1):
    if str1[0]=="insert":
        l.insert(int(str1[1]),int(str1[2]))
    elif str1[0]=="print":
        print(l)
    elif str1[0]=="append":
        l.append(int(str1[1]))
    elif str1[0]=="sort":
        l.sort()
    elif str1[0]=="pop":
        l.pop()
    elif str1[0]=="reverse":
        l.reverse()
    elif str1[0]=="remove":
        l.remove(int(str1[1]))
    return l
li=[] 
n = int(input())
for i in range(n):
    s=input().split()
    p=oper(li,s)