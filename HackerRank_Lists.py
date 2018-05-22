# -*- coding: utf-8 -*-
"""
#################################
# Hacker Rank Designer Lists #
#################################

Consider a list (list = []). You can perform the following commands:

  1) insert i e: Insert integer `e` at position `i`.
  2) print: Print the list.
  3) remove e: Delete the first occurrence of integer `e`.
  4) append e: Insert integer `e` at the end of the list.
  5) sort: Sort the list.
  6) pop: Pop the last element from the list.
  7) reverse: Reverse the list.
    
Initialize your list and read in the value of `n` followed by `n` lines of 
commands where each command will be of the 7 types listed above. Iterate 
through each command in order and perform the corresponding operation on your 
list.


Input Format:
  The first line contains an integer, `n`, denoting the number of commands. 
  Each line `i` of the `n` subsequent lines contains one of the commands 
  described above.

Constraints:
  The elements added to the list must be integers.

Output Format:
  For each command of type `print`, print the list on a new line.
  
"""

alist = []
for i in range(int(raw_input())): # first input is N
    
    # convert to list based on space 
    command = raw_input().split()
    
    # convert index 1 to end to integers 
    for index in range(1,len(command)): 
        command[index] = int(command[index])
        
    if command[0] == 'insert': 
        alist.insert(command[1],command[2])
    elif command[0] == 'print': 
        print alist
    elif command[0] == 'remove': 
        alist.remove(command[1])
    elif command[0] == 'append': 
        alist.append(command[1])
    elif command[0] == 'sort': 
        alist.sort()
    elif command[0] == 'pop':
        alist.pop()
    elif command[0] == 'reverse': 
        alist.reverse() 
        
