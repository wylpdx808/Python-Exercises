# -*- coding: utf-8 -*-
"""
#################################
# Hacker Rank String Validators #
#################################

You are given a string `S`. 
Your task is to find out if the string `S` contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.


Input Format:
  A single line containing a string `S`.

Constraints:
  0 < len(S) < 1000

Output Format: 
  In the first line, print True if `S` has any alphanumeric characters. 
  Otherwise, print False. 
  In the second line, print True if `S` has any alphabetical characters. 
  Otherwise, print False. 
  In the third line, print True if  `S`has any digits. Otherwise, print False. 
  In the fourth line, print True if `S` has any lowercase characters. 
  Otherwise, print False. 
  In the fifth line, print True if `S` has any uppercase characters. 
  Otherwise, print False.

"""

# Hacker Rank string validators
s = raw_input()
print any(letter.isalpha() for letter in s)
print any(letter.isalpha() for letter in s)
print any(letter.isdigit() for letter in s)
print any(letter.islower() for letter in s)
print any(letter.isupper() for letter in s)
 
# another solution 
s = raw_input()
alnum = []
alpha = []
digits = []
lower = []
upper = []
for letter in s:
    if letter.isalnum():
        alnum.append(letter)
        if letter.isalpha():
            alpha.append(letter)
            if letter.islower():
                lower.append(letter)
            elif letter.isupper():
                upper.append(letter)
        elif letter.isdigit():
            digits.append(letter)

if len(alnum) > 0:
    print True
else:
    print False
if len(alpha) > 0:
    print True
else:
    print False
if len(digits) > 0:
    print True
else:
    print False
if len(lower) > 0:
    print True
else:
    print False
if len(upper) > 0:
    print True
else:
    print False