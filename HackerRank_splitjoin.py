# -*- coding: utf-8 -*-
"""
##############################
# Hacker Rank Split and Join #
##############################

You are given a string. Split the string on a " " (space) delimiter and join 
using a - hyphen.

Input Format:
  The first line contains a string consisting of space separated words.

Output Format:
  Print the formatted string as explained above.

"""

s = raw_input()
def split_and_join(line):
    splitstring = line.split(' ')
    joinstring = '-'.join(splitstring)
    return joinstring 

print split_and_join(s)