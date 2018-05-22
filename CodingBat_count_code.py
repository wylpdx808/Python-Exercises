# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:03:09 2018

@author: Wai Yan
"""

# CodingBat Python count_code Exercise 
def count_code(str): # list comp
    lst = [str[x:x+4] for x in range(len(str))]
    codelist = [word for word in lst if word[0] == 'c' and word[1] == 'o' and word[3] == 'e']
    return len(codelist)
print count_code('coze')
