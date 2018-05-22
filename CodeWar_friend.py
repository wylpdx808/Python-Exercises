# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar friend challenge
def friend(x):
    return [name for name in x if len(name) == 4]

print friend(["Ryan", "Kieran", "Mark",])