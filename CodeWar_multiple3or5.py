# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# CodeWar multiple 3 or 5 
def solution(number): 
    multiple = [i for i in range(1,number) if i % 3 == 0 or i % 5 == 0]
    return sum(set(multiple)) 

print solution(10)
print solution(100)