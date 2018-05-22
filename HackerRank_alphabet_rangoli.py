# -*- coding: utf-8 -*-
"""
##########################################
# Hacker Rank Alphabet Rangoli Challenge #
##########################################

You are given an integer, N. Your task is to print an alphabet rangoli of 
size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

The center of the rangoli has the first alphabet letter a, and the boundary has
the Nth alphabet letter (in alphabetical order).


Input Format:
  Only one line of input containing , the size of the rangoli.

Constraints:
  0 < N < 27
    
Output Format:
  Print the alphabet rangoli in the format explained above.

"""

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    n = size
    L = []
    for i in range(n):
        s = '-'.join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n - 3, '-'))
    print '\n'.join(L[:0:-1] + L)

print_rangoli(5)