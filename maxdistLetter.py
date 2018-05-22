# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:19:48 2018

@author: Wai Yan
"""

# another way to do coding challenge (number of letters between farthest apart letters)
def maxdistLetter(): 
    my_string = raw_input('Enter a word: ') 
    first_dict = {}
    last_dict = {}

    for i in range(len(my_string)): 
        if my_string[i] not in first_dict.keys(): 
            first_dict[my_string[i]] = i 
        else: 
            last_dict[my_string[i]] = i

    lastValues = last_dict.keys() 
    
    distance = [] 
    for letter in lastValues: 
        letterdist = last_dict[letter] - first_dict[letter]
        distance.append(letterdist)
    
    #print first_dict
    #print last_dict 
    #print distance 
    
    return max(distance) - 1
    
print maxdistLetter()