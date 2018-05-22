# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:01:40 2018

@author: Wai Yan
"""

str = 'abc hi ho'
twoletters = []
for i in range(len(str)): # no list comp
    twoletters.append(str[i:i+2])
print twoletters.count('hi')
