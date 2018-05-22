# -*- coding: utf-8 -*-
"""
######################
# Hacker Rank Day 11 #
######################

Context:
  Given a 6x6 2D Array, `A`:

  1 1 1 0 0 0
  0 1 0 0 0 0
  1 1 1 0 0 0
  0 0 0 0 0 0
  0 0 0 0 0 0
  0 0 0 0 0 0
  
  We define an hourglass in `A` to be a subset of values with indices falling 
  in this pattern in `A`'s graphical representation:

  a b c
    d
  e f g
  
  There are 16 hourglasses in `A`, and an hourglass sum is the sum of an 
  hourglass' values.

Calculate the hourglass sum for every hourglass in `A`, then print the maximum 
hourglass sum.


Input Format:
  There are 6 lines of input, where each line contains 6 space-separated 
  integers describing 2D Array `A`; every value in `A` will be in the inclusive 
  range of -9 to 9.

Constraints:
  -9 <= A[i][j] <= 9
  0 <= i,j <= 5

Output Format: 
  Print the largest (maximum) hourglass sum found in `A`.
  
  
"""

def maxHGsum(A): 
    A_dict = {}
    i = 1 
    for m in range(0, len(A)-2): 
        for n in range(0, len(A[m])-2): 
            first = A[m][n] + A[m][n+1] + A[m][n+2]
            second = A[m+1][n+1]
            third = A[m+2][n] + A[m+2][n+1] + A[m+2][n+2]
            sumALL = first + second + third 
            A_dict[i] = sumALL
            i += 1 
    hourglass_sums = A_dict.values()
    return max(hourglass_sums)
    

import sys

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
    
print maxHGsum(arr)
