# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar Find the missing letter 
def find_missing_letter(chars): 
    import string 
    alpha = string.ascii_lowercase + string.ascii_uppercase
    
    start = alpha.find(chars[0])
    L = alpha[start:start + len(chars) + 1]
        
    for a in L: 
        if a not in chars: 
            return a 
 
print find_missing_letter(['O','Q','R','S'])