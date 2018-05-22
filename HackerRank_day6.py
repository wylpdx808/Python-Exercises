# -*- coding: utf-8 -*-
"""
#####################
# Hacker Rank Day 6 #
#####################

Given a string, `S`, of length `N` that is indexed from 0 to N-1, print its 
even-indexed and odd-indexed characters as 2 space-separated strings on a 
single line.

Note: 0 is considered to be an even index.


Input Format:
  The first line contains an integer, `T` (the number of test cases). 
  Each line `i` of the `T` subsequent lines contain a String, `S`.

Constraints:
  1 <= T <= 10 
  2 <= length of S <= 10000

Output Format:

  For each String `Sj` (where 0 <= j <= T-1), print `Sj`'s even-indexed 
  characters, followed by a space, followed by `Sj`'s odd-indexed characters.

"""

T = int(raw_input())
for i in range(T): 
    S = raw_input()
    even = []
    odd = []
    for n in range(len(S)): 
        if n % 2 == 0: 
            even.append(S[n])
        else: 
            odd.append(S[n])
    print "".join(even), "".join(odd)