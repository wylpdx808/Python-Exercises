# -*- coding: utf-8 -*-
"""
########################################
# Hacker Rank Find the Runner-Up Score #
########################################

Given the participants' score sheet for your University Sports Day, you are 
required to find the runner-up score. You are given `n` scores. Store them in 
a list and find the score of the runner-up.


Input Format:
  The first line contains `n`. The second line contains an array `A`[]  of `n` 
  integers each separated by a space.

Constraints:
  2 <= n <= 10
  -100 <= A[i] <= 100

Output Format: 
  Print the runner-up score.

"""

n = int(raw_input())
arr = map(int, raw_input().split())
    
maximum = max(arr)
newarr = [score for score in arr if score != maximum]
        
runnerup = max(newarr)
print runnerup