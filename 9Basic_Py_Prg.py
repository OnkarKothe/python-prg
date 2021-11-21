# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:45:55 2021

@author: Onkar
"""
'''
#1 print prime number from 100 to 200

for n in range(100,200):
    if all(n%i!=0 for i in range(2,n)):
        print(n)

#2 sort fuction to sort element in a list

l=[12,13,14,1,3,2]
l.sort(reverse=True)
print(l)

#without using sort function
l=[12,13,14,1,3,2]
lm=[]
while l:
    s=l[0]
    for x in l:
        if x>s:
            s=x
    lm.append(s)
    l.remove(s)
print(lm)

#3 fibo series
def f(n):
    if n==0: return 0
    elif n==1: return 1
    else: return f(n-1)+f(n-2)
for i in range(0,12):
    print(f(i),end=" ")

#4 reverse list
l=[1,2,10,4,5,6]
print(l[::-1])

#5 palindrome or not
def pal(n):
    rev=''.join(reversed(n))
    if (n== rev):
        return True
    return False
i=input()
print(pal(i))

#6 set of duplicates
l=[1,1,2,2,3,3,4,4,5,5,6]
print(set([x for x in l if l.count(x)>1]))

#7 print num of word in a given array
s="i am ok"
print(len(s.split()))

#8 search a given element
def arr(n,x):
    for i in range(len(n)):
        if n[i]==x:
            return 1
    print("not present")
n=[1,2,3,4,5,6,5,6,1]
print(arr(n,5))

#9 list compr print square 1 to 10 even numbers
l=[x*x for x in range(1,11)if x%2==0]
print(l)
'''
