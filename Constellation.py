
# -*- coding: utf-8 -*-
'''
Three characters { #, *, . } represents a constellation of stars and galaxies in space.
Each galaxy is demarcated by # characters. There can be one or many stars in a given galaxy.
Stars can only be in the shape of vowels { A, E, I, O, U }. A collection of * in the shape of the vowels is a star.
A star is contained in a 3×3 block. Stars cannot be overlapping. The dot(.) character denotes empty space.
Example:

Input

18

* . * # * * * # * * * # * * * . * .

* . * # * . * # . * . # * * * * * *

* * * # * * * # * * * # * * * * . *

Output

U#O#I#EA

'''
"""
Created on Fri Nov 12 22:45:43 2021

@author: Onkar
"""

n=int(input())
co=[]
for i in range(3):co.append(list(input().split()))
print(co)
i=0
while i<n-2:
    if co[0][i]=='#':
        print("#",end="")
        i+=1
        continue
    if co[0][i]=='.' and co[0][i+1]=='*' and co[0][i+2]=='.':
        if co[1][i]=='*' and co[1][i+1]=='*' and co[1][i+2]=='*':
            if co[2][i]=='*' and co[2][i+1]=='.' and co[2][i+2]=='*':
                print("A",end="")
    if co[0][i]=='*' and co[0][i+1]=='*' and co[0][i+2]=='*':
        if co[1][i]=='*' and co[1][i+1]=='*' and co[1][i+2]=='*':
            if co[2][i]=='*' and co[2][i+1]=='*' and co[2][i+2]=='*':
                print("E",end="")
                i+=1
        elif co[1][i]=='.' and co[1][i+1]=='*' and co[1][i+2]=='.':
            if co[2][i]=='*' and co[2][i+1]=='*' and co[2][i+2]=='*':
                print("I",end="")
                i+=1
        elif co[1][i]=='*' and co[1][i+1]=='.' and co[1][i+2]=='*':
            if co[2][i]=='*' and co[2][i+1]=='*' and co[2][i+2]=='*':
                print("O",end="")
                i+=1
    if co[0][i]=='*' and co[0][i+1]=='.' and co[0][i+2]=='*':
        if co[1][i]=='*' and co[1][i+1]=='.' and co[1][i+2]=='*':
            if co[2][i]=='*' and co[2][i+1]=='*' and co[2][i+2]=='*':
                print("U",end="")
                i+=1
    i+=1
