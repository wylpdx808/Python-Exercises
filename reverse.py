# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:10:18 2018

@author: Wai Yan
"""

def reverse(text): 
  textlen=len(text)
  revtext = ''
  for n in range(0,textlen):
    revtext += text[textlen-1]
    textlen -= 1
  return revtext
    
print reverse('abcdefghijklmnopqrstuvwxyz')
