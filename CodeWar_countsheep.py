# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar count sheep challenge 
def count_sheeps(arrayOfSheeps):
    count = 0 
    for sheep in arrayOfSheeps:
        if sheep == True:
            count += 1 
    return count 

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]
print count_sheeps(array1)