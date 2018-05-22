# -*- coding: utf-8 -*-
"""
#########################
# Hacker Rank Text Wrap #
#########################

You are given a string `S` and width `w`. 
Your task is to wrap the string into a paragraph of width `w`.


Input Format:
  The first line contains a string, `S`. 
  The second line contains the width, `w`.

Constraints: 
  0 < len(S) < 1000
  0 < w < len(S)

Output Format: 
  Print the text wrapped paragraph.

"""

import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

string, max_width = raw_input(), int(raw_input())
result = wrap(string, max_width)
print result 