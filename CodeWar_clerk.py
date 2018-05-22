# -*- coding: utf-8 -*-
"""
#########################
# CodeWar Vasya - Clerk #
#########################

The new "Avengers" movie has just been released! There are a lot of people at 
the cinema box office standing in a huge line. Each of them has a single 100, 
50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every 
single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has 
no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with 
the bills he has at hand at that moment. Otherwise return NO.

Examples:

    tickets([25, 25, 50]) # => YES 
    tickets([25, 100]) 
         # => NO. Vasya will not have enough money to give change to 100 dollars
         
"""

def tickets(people):
    bills = []
    for person in people: 
        change = person - 25 
        if change == 0: # bill is 25 
            bills.append(person)
        elif change == 25: # bill is 50 
            if 25 in bills:
                bills.append(person)
                bills.remove(25)
            else:
                return 'NO'
                break
        elif change == 75: # bill is 100
            if (25 in bills and 50 in bills):
                bills.append(person)
                bills.remove(25)
                bills.remove(50)
            elif bills.count(25) == 3: 
                bills.append(person)
                for i in range(3): 
                    bills.remove(25)
            else: 
                return 'NO'
                break
    return 'YES'

print tickets([25,25,50])


