# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:02:08 2018

@author: Wai Yan
"""

# CodingBat Python String-2 cat_dog exercise
def cat_dog(str): # list comp
    lst = [str[i:i+3] for i in range(len(str))]
    cat = lst.count('cat')
    dog = lst.count('dog')
    print lst
    if cat == dog: 
        return True 
    else: 
        return False 

print cat_dog('1cat1cadodog')