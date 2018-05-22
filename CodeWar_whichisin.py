# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar Which is in? 

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]   

r = []
for subword in a1:
    for word in a2:
        if subword in word: 
            r.append(subword)
            
R = list(set(r))
R.sort()
print R