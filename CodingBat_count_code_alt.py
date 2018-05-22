# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:04:03 2018

@author: Wai Yan
"""

def count_code2(str): # no list comp
    list = []
    for i in range(len(str)): 
        list.append(str[i:i+4])
    codelist = []
    for word in list: 
        if word[0] == 'c' and word[1] == 'o' and word[3] == 'e': 
            codelist.append(word)
    return len(codelist)
print count_code2('cooocooecopecooe')