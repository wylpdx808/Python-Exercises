# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:10:18 2018

@author: Wai Yan
"""

sentence = 'hello my name is pat hello'

def censor(text, word): 
  textsplit = text.split()
  astk_len = len(word)
  for n in range(len(textsplit)): 
    if textsplit[n] == word: 
      textsplit[n] = '*' * astk_len
    #else: 
      #continue
      
  text = " ".join(textsplit)
  return text 
  
newsent = censor(sentence, 'hello')
print newsent