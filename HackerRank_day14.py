# -*- coding: utf-8 -*-
"""
######################
# Hacker Rank Day 14 #
######################

Complete the Difference class by writing the following:
  A class constructor that takes an array of integers as a parameter and saves 
  it to the `elements` instance variable.
  A `computeDifference` method that finds the maximum absolute difference 
  between any numbers in `N` and stores it in the `maximumDifference` instance 
  variable.


Input Format:
  You are not responsible for reading any input from stdin. The locked Solution 
  class in your editor reads in 2 lines of input; the first line contains `N`, 
  and the second line describes the `elements` array.

Constraints:
  1 <= N <= 10
  1 <= elements[i] <= 100, where 0 <= i <= N-1 
  
Output Format: 
  You are not responsible for printing any output; the Solution class will 
  print the value of the `maximumDifference` instance variable.


"""

class Difference(object): 
    def __init__(self,elements): 
        self.elements = elements 
    def computeDifference(self): 
        self.min = min(self.elements)
        self.max = max(self.elements) 
        self.maximumDifference = abs(self.max - self.min)
        return self.maximumDifference
        
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference