# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar DNA challenge 
def DNA_strand(dna):
    dnakey = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join([dnakey[letter] for letter in dna])

print DNA_strand('ATTGC')
