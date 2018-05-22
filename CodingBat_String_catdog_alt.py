# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:02:46 2018

@author: Wai Yan
"""

def cat_dog2(str): 
    catdoglist = [] # no list comp 
    for i in range(len(str)): 
        catdoglist.append(str[i:i+3])
    catcount = catdoglist.count('cat')
    dogcount = catdoglist.count('dog')
    if catcount == dogcount: 
        return True
    else: 
        return False 
print cat_dog2('1cat1cadodog')
