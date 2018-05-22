# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:25:29 2018

@author: Wai Yan
"""

def changevowelstring(my_string): 
    stringlist = []
    for letter in my_string: 
        stringlist.append(letter)
    
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new_stringlist = []
    for i in range(len(stringlist)): 
        if stringlist[i] in vowels: 
            new_stringlist.append('*')
        else: 
            new_stringlist.append(stringlist[i])
    new_string = ''.join(new_stringlist)
    return new_string
    
            
print changevowelstring('superdupercool')