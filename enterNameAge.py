# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:21:54 2018

@author: Wai Yan
"""

def enterNameAge(): 
    name = raw_input("Enter name: ")
    age = int(raw_input("Enter age: "))
    yrto100 = 100 - age 
    
    from datetime import datetime 
    now = datetime.now() 
    year100 = now.year + yrto100
    
    return "Hello %s, you will turn 100 years old in %s" % (name, str(year100))

print enterNameAge()