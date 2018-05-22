# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:29:53 2018

@author: Wai Yan
"""

# Codewar song decoder 
def song_decoder(song): 
    noWUB = song.split('WUB')
    return ' '.join(filter(None, noWUB))
    

print song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")

# another solution 
def song_decoder2(song): 
    noWUB = song.replace('WUB', ' ')
    print noWUB
    return ' '.join(noWUB.split())
    
noWUB = song_decoder2('WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB')  