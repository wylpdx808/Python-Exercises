# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:23:46 2018

@author: Wai Yan
"""

def changevowel(my_list): 
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(my_list)): 
        if my_list[i] in vowels: 
            my_list[i] = '*'
    return my_list 

print changevowel(['h','e','l','l','o'])