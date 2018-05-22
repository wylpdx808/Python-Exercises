# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar Likes
def likes(names): 
    if len(names) == 0: 
        return "no one likes this"
    elif len(names) == 1: 
        return "{} likes this".format(names[0]) 
    elif len(names) == 2: 
        return "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3: 
        return "{}, {}, and {} like this".format(names[0], names[1], names[2])
    else: 
        return "{}, {}, and {} others like this".format(names[0], names[1], len(names)-2)
    
print likes(['Alex', 'Jacob', 'Mark', 'Max'])



