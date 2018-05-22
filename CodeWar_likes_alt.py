# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar Likes
def likes(names): 
    n = len(names) 
    return {
            0: 'no one likes this', 
            1: '{} likes this', 
            2: '{} and {} like this', 
            3: '{}, {} and {} like this', 
            4: '{}, {} and {others} others like this'
    }[min(4,n)].format(*names[:3], others = n-2)

    
print likes(['peter','alex','jacob', 'mark', 'adam'])
