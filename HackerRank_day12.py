# -*- coding: utf-8 -*-
"""
######################
# Hacker Rank Day 12 #
######################

You are given two classes, Person and Student, where Person is the base class 
and Student is the derived class. Completed code for Person and a declaration 
for Student are provided for you in the editor. Observe that Student inherits 
all the properties of Person.

Complete the Student class by writing the following:
  A Student class constructor, which has 4 parameters:
    1) A string, `firstName`.
    2) A string, `lastName`.
    3) An integer, `id`.
    4) An integer array (or vector) of test scores, `scores`.
    
  A char `calculate()` method that calculates a Student object's average and 
  returns the grade character representative of their calculated average:      
    Letter   Average (a) 
      O     90 <= a <= 100
      E     80 <= a < 90
      A     70 <= a < 80
      P     55 <= a < 70
      D     40 <= a < 55
      T           a < 40


Input Format:
  The locked stub code in your editor calls your Student class constructor and 
  passes it the necessary arguments. It also calls the calculate method (which 
  takes no arguments).

  You are not responsible for reading the following input from stdin: 
  The first line contains `firstName`, `lastName`, and `id`, respectively. 
  The second line contains the number of test scores. The third line of 
  space-separated integers describes `scores`.

Constraints:
  1 <= |firstName|,|lastName| <= 10
  |id| = 7
  0 <= score, average <= 100
    
Output Format:
  This is handled by the locked stub code in your editor. 
  Your output will be correct if your Student class constructor and 
  `calculate()` method are properly implemented.



"""

class Person(object): 
    def __init__(self, firstName, lastName, idNumber, scores): 
        self.firstName = firstName 
        self.lastName = lastName 
        self.idNumber = idNumber

class Student(Person): 
    def __init__(self, firstName, lastName, idNumber, scores): 
        self.firstName = firstName 
        self.lastName = lastName 
        self.idNumber = idNumber
        self.scores = scores 
        
    def calculate(self, scores): 
        average = sum(self.scores)/float(len(self.scores)) 
        if average >= 90: 
            return "O"
        elif average >= 80: 
            return "E"
        elif average >= 70: 
            return "A"
        elif average >= 55: 
            return "P"
        elif average >= 40: 
            return "D" 
        else: 
            return "T" 