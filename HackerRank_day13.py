# -*- coding: utf-8 -*-
"""
######################
# Hacker Rank Day 13 #
######################

Given a Book class and a Solution class, write a MyBook class that does the 
following:

  Inherits from Book
  Has a parameterized constructor taking these 3 parameters:
    1) string `title`
    2) string `author`
    3) int `price`
    
  Implements the Book class' abstract `display()` method so it prints these 
  3 lines:
    1) Title:, a space, and then the current instance's `title`.
    2) Author:, a space, and then the current instance's `author`.
    3) Price:, a space, and then the current instance's `price`.
  Note: Because these classes are being written in the same file, you must not 
  use an access modifier (e.g.: `public`) when declaring MyBook or your code 
  will not execute.


Input Format:
  You are not responsible for reading any input from stdin. The Solution class 
  creates a Book object and calls the MyBook class constructor (passing it the 
  necessary arguments). It then calls the display method on the Book object.

Output Format:
  The `voiddisplay()` method should print and label the respective `title`, 
  `author`, and `price` of the MyBook object's instance (with each value on its 
  own line) like so:

    Title: $title
    Author: $author
    Price: $price
    
  Note: The `$` is prepended to variable names to indicate they are 
  placeholders for variables.
  
"""

from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

# Write MyBook class
class MyBook(Book): 
    def __init__(self,title,author,price): 
        self.title = title 
        self.author = author 
        self.price = price 
        
    def display(self): 
        print "Title:", self.title 
        print "Author:", self.author 
        print "Price:", self.price 
        
title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()
    