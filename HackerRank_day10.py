# -*- coding: utf-8 -*-
"""
######################
# Hacker Rank Day 10 #
######################

Given a base-10 integer, `n`, convert it to binary (base-2). Then find and 
print the base-10 integer denoting the maximum number of consecutive 1's in 
`n`'s binary representation.


Input Format:
  A single integer, `n`.

Constraints:
  1 <= n <= 10e6

Output Format:
  Print a single base-10 integer denoting the maximum number of consecutive 1's 
  in the binary representation of `n`.

"""

def consecutiveOnes(n): 
    base2 = bin(n)
    numbers = base2[2:len(base2)]
    ones = numbers.split("0")
    
    max = 0 
    for i in range(len(ones)): 
        if len(ones[i]) > max: 
            max = len(ones[i]) 
            
    return max 

import sys
n = int(raw_input().strip())  
print consecutiveOnes(n)