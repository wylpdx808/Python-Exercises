# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:10:18 2018

@author: Wai Yan
"""

def anti_vowel(text): 
  vowels = ['a','e','i','o','u']
  no_vowels = ''
  for letter in text: 
    if letter not in vowels: 
      no_vowels += letter 
    else: 
      pass 
  return no_vowels 

print anti_vowel('Hey You!')