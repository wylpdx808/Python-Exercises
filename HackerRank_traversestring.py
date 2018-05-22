# -*- coding: utf-8 -*-
"""
##############################
# Hacker Rank Traverse String #
##############################

In this challenge, the user enters a string and a substring. You have to print 
the number of times that the substring occurs in the given string. String 
traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.


Input Format:
  The first line of input contains the original string. The next line contains 
  the substring.

Constraints: 
  1 <= len(string) <= 200
  Each character in the string is an ascii character.

Output Format:
  Output the integer number indicating the total number of occurrences of the 
  substring in the original string.

"""

def count_substring(string,sub_string): 
    words = [string[i:i+len(sub_string)] for i in range(len(string))]
    return words.count(sub_string)
    
string = 'ABCDCDC'
sub_string = 'CDC'
print count_substring(string, sub_string)
