# -*- coding: utf-8 -*-
"""
#####################
# Hacker Rank Day 7 #
#####################

Given an array, `A`, of `N` integers, print `A`'s elements in reverse order as 
a single line of space-separated numbers.


Input Format:
  The first line contains an integer, `N` (the size of our array). 
  The second line contains `N` space-separated integers describing array `A`'s 
  elements.

Constraints:
  1 <= N <= 1000
  1 <= Ai <= 1000, where `Ai` is the `ith` integer in the array.
  
Output Format:
  Print the elements of array `A` in reverse order as a single line of
  space-separated numbers.


"""

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

for i in range(n-1,-1,-1): 
    print arr[i],