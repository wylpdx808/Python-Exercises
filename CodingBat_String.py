# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:59:07 2018

@author: Wai Yan
"""

# CodingBat Python String exercise
def double_char(str): 
    char2 = [x*2 for x in str]
    return ''.join(char2)

print double_char('Theta')