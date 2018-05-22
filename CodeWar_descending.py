# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar descending order
def descending(num): 
    nslist = list(str(num))
    nslist.sort()
    return int(''.join(nslist[::-1]))

print descending(56787654)


