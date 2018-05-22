# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar phone number 
def create_phone_number(n):
    N = [str(i) for i in n]
    return "(%s) %s-%s" %("".join(N[0:3]), "".join(N[3:6]), "".join(N[6:]))

print type(create_phone_number(n))