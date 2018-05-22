# -*- coding: utf-8 -*-
"""
###########################
# Hacker Rank Nested List #
###########################

Given the names and grades for each student in a Physics class of `N` students, 
store them in a nested list and print the name(s) of any student(s) having the 
second lowest grade.

Note: If there are multiple students with the same grade, order their names 
alphabetically and print each name on a new line.


Input Format:
  The first line contains an integer, `N`, the number of students. 
  The `2N` subsequent lines describe each student over 2 lines; the first line 
  contains a student's name, and the second line contains their grade.

Constraints:
  2 <= N <= 5
  There will always be one or more students having the second lowest grade.
  
Output Format: 
  Print the name(s) of any student(s) having the second lowest grade in 
  Physics; if there are multiple students, order their names alphabetically 
  and print each one on a new line.

"""

students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])

minscore = min([score[1] for score in students])
students_sub = [x for x in students if x[1] != minscore]

minscore2 = min([score2[1] for score2 in students_sub])
runner_up = [y for y in students_sub if y[1] == minscore2]
runner_up.sort()

for student in runner_up: 
    print student[0]


# a better way to do above 
a = [[raw_input(), float(raw_input())] for x in range(int(raw_input()))]
scores = sorted(set([x[1] for x in a]))

lowscore2 = [x[0] for x in a if x[1] == scores[1]]

for score in lowscore2: 
    print score 