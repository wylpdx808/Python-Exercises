# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar delete nth 

def delete_nth(order, max_e): 
    newlst = []
    for i in order: 
        if newlst.count(i) < max_e: 
            newlst.append(i)
    return newlst

test1 = delete_nth([14, 29, 10, 30, 9, 30, 26, 11, 14, 31, 31, 11, 29, 11, 14, 
                    30, 9, 10, 26, 15, 15, 9, 7, 26, 15, 9, 14, 31, 14, 9, 31, 
                    31, 31, 10, 7, 29, 10, 9, 31, 14, 29, 31, 7, 26, 26, 10, 
                    14, 31, 26, 10, 10, 10, 11],2)
