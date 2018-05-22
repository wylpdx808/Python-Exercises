# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar string_splosion
def string_splosion(str):
    new = []
    for i in range(len(str)): 
      new.append(str[0:i+1])
    return ''.join(new)


print string_splosion('Code')