# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:05:38 2018

@author: Wai Yan
"""

# DataCamp List Comprehension Exercise 
sentence = 'the quick brown fox jumps over the lazy dog'
words = sentence.split()

# list comp
word_lengths = [len(word) for word in words if word != 'the']
print word_lengths
# no list comp
lengthword = []
for word in words: 
    if word != 'the': 
        lengthword.append(len(word))
print lengthword