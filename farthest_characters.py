# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:07:39 2018

@author: Wai Yan
"""

def farchar(str): 
    first, last, dist = {}, {}, {}
    for i,c in enumerate(str): 
        if c not in first.keys(): 
            first[c] = i 
        else: 
            last[c] = i 
    
    if len(last) == 0: 
        return [None, None]
    else: 
        for x in last: 
            dist[x] = last[x] - first[x]
        
        maxdist = max(dist.values())
    
        for n in dist: 
            if dist[n] == maxdist: 
                return "{}: [{}, {}]" .format(n, first[n], last[n])
    
        
dictionary =  farchar('eaasdsdfadfdgsasdffffde')