# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:00:59 2021

@author: Onkar
"""
'''
     #1 check num is +
d=[1,2,3,-4,-6]
for idx,num in enumerate(d):
    if num<0:
        d[idx]=0
print(d)
'''
'''
     #2 generators consume less memory

import sys
l=(x for x in range(10000))
print(sum(l))
print(sys.getsizeof(l),"bytes")

     #output:
     #49995000
     #112 bytes

m=[i for i in range(10000)]
print(sum(m))
print(sys.getsizeof(m),"bytes")

     #output:
     #49995000
     #87616 bytes

'''
'''
     #3 count duplications 
from collections import Counter
l=[1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,4,3,2,1,6]
counter=(Counter(l))
print(counter)

     #output: 
     #Counter({1: 5, 2: 4, 3: 4, 4: 4, 5: 2, 6: 1})
     
cou=counter.most_common(1)
print(cou)
     #output:
     #[(1, 5)]
'''
'''
     #4 format string with f-string
name="alex"
st=f"Hello {name}"
print(st)

     #output:Hello alex

i=10
print(f"{i} square is {i*i}")
     #output:10 square is 100
'''
'''
     #5 merge dictionary
d1={"name":"ok","age":22}
d2={"name":"ok","city":"solap"}
merge={**d1,**d2}
print(merge)

#output:{'name': 'ok', 'age': 22, 'city': 'solap'}
'''
