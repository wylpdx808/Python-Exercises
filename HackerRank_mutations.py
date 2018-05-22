# -*- coding: utf-8 -*-
"""
#################################
# Hacker Rank Mutations #
#################################

Read a given string, change the character at a given index and then print the 
modified string.


Input Format:
  The first line contains a string, `S`. 
  The next line contains an integer `i`, denoting the index location and a 
  character `c` separated by a space.

Output Format:
  Using any of the methods explained above, replace the character at index `i` 
  with character `c`.

"""

def mutate_string(string, position, character):
    slist = list(string)
    slist[position] = character
    joined = ''.join(slist)
    return joined 

s = raw_input() 
i, c = raw_input().split() 
s_new = mutate_string(s, int(i), c)
print s_new