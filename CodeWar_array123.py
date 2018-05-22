# -*- coding: utf-8 -*-
"""


"""

# Codewar array123
def array123(nums):
  arr = [str(i) for i in nums]
  Arr = ','.join(arr)
  a = '1,2,3'
  if a in Arr: 
    return True 
  else: 
    return False 
  
hello = array123([1, 1, 2, 1, 2, 3])