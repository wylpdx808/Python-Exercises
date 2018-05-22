# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:36:27 2018

@author: Wai Yan
"""

def repVowels(my_list): 
    for i in range(len(my_list)): 
        if my_list[i] in vowels: 
            my_list[i] = '*'
        else: 
            continue 
    return my_list
        
hellolist = repVowels(['h','e','l','l','o'])
print hellolist