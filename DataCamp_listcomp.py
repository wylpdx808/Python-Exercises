# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:06:40 2018

@author: Wai Yan
"""

# Hacker Rank Challenge List Comprehensions 

x = int ( raw_input())
y = int ( raw_input())
n = int ( raw_input())
ar = []

# non-list comprehension
for i in range ( x + 1 ) :
    for j in range( y + 1):
        if i+j != n:
            ar.append([i,j])
print ar    

# list comprehension method
print [[i,j] for i in range(x+1) for j in range(y+1) if (i+j) != n]