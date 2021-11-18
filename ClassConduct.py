# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:47:02 2021

@author: Onkar
"""
'''
a discrit maths professor has a class of student, 
fustrated with thier lack of attendance,
he decided to cancel the class if the student will fewer 
then the sum number of students are present when the class start
write a prg to print if the class should be canvcelled or not,
bassed on the following inputs.
input:
    n = num of student
    k=min num of student 
    arival tym
'''
n=int(input("num of student"))
k=int(input("min stud req"))
c=0
if n>=k:
    l=[int(x) for x in input().split()]
    for i in range(n):
        if l[i]<1:
            c+=1
    if c>=k:
        print("class will b conducted")
    else:
        print("class will not be conducted")
else:
    print("num of stud should be more than min stud req")