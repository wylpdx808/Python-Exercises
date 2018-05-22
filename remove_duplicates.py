# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:59:44 2018

@author: Wai Yan
"""

def remove_duplicates(alist): 
  dupdict = {}
  for i in alist: 
    if i not in dupdict.keys(): 
      dupdict[i] = 1 
    else: 
      continue 
      
  nondupelist = []
  for n in dupdict: 
    nondupelist.append(n)
    
  return nondupelist
  
thislist=[3,4,5,5,4,6,7,8]
newlist = remove_duplicates(thislist)
print newlist