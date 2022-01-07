"""
Created on Fri Jan  7 16:54:08 2022

@author: Onkar
"""
'''
Write a python function, check_anagram() which accepts two strings and returns True, 
if one string is a special anagram of another string. Otherwise returns False.

The two strings are considered to be a special anagram if they contain repeating 
characters but none of the characters repeat at the same position. 
The length of the strings should be the same.

Note: Perform case insensitive comparison wherever applicable.

Sample Input           Expected Output

eat, tea               True

backward,drawback      False (Reason: character 'a' repeats at position 6, not an anagram)

Reductions,discounter  True

About, table           False
'''
def check_anagram(data1,data2):
  if len(data1)==len(data2):  
    se=set((data1+data2).lower())
    for i in se:
        if (data1.lower()).count(i)!= (data2.lower()).count(i):
           return False
    for j in range(len(data1)):
        if data1[j]==data2[j]:
            return False
  else:
      return False
  return True
print(check_anagram("eat","tea"))