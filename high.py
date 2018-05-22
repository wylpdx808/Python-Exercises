# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:08:42 2018

@author: Wai Yan
"""

def high(x): 
    import string 
    alpha = string.ascii_lowercase
    
    # make alphabet dictionary 
    alphadict = {}
    for i, c in enumerate(alpha, 1): 
        alphadict[c] = i 
    
    # make scoreboard of words 
    x = x.split()

    scoreboard = {}
    for word in x: 
        score = 0 
        for letter in word: 
            score += alphadict[letter] 
        scoreboard[word] = score 
        
    maxscore = max(scoreboard.values())
   
    # get indices of words with max score 
    maxwords = {}
    for m in scoreboard: 
        if scoreboard[m] == maxscore: 
            maxwords[x.index(m)] = m
    
    return x[min(maxwords)]


scoreboard = high('man nam amn') 