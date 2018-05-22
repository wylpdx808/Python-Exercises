# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:19:08 2018

@author: Wai Yan
"""

def changeVowel(my_stringlist):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    new_stringlist = []
    
    for i in range(len(my_stringlist)): 
        if my_stringlist[i] in vowels: 
            new_stringlist.append('*')
        else: 
            new_stringlist.append(my_stringlist[i])
            
    return new_stringlist
    
    
blah = ['h','e','l','l','o','b','l','a','h']
    
changeVowel(blah)