# -*- coding: utf-8 -*-
"""
#########################
# Hacker Rank sWAP cASE #
#########################

You are given a string and your task is to swap cases. In other words, convert 
all lowercase letters to uppercase letters and vice versa.

For Example:

    Www.HackerRank.com → wWW.hACKERrANK.COM
    Pythonist 2 → pYTHONIST 2
    
    
Input Format: 
  A single line containing a string `S`.

Constraints: 
  0 < len(S) <= 1000

Output Format: 
  Print the modified string `S`.

"""

def swap_case(s): 
    newstring = []
    for letter in s: 
        if letter.isupper(): 
            newstring.append(letter.lower())
        elif letter.islower(): 
            newstring.append(letter.upper())
        else: 
            newstring.append(letter)
    return "".join(newstring)
            
print swap_case('Swap Case')