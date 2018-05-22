# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar is_kiss
def is_kiss(words): 
    wlist = words.split(' ')
    for word in wlist: 
        if len(word) > len(wlist): 
            return "Keep It Simple Stupid"
            break
    return "Good work Joe!" 
