# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:22:04 2016


"""
########################################################
#
# Compter Project 11
#
#Use data files to create class averages
#
#######################################################
'''
import classes and open data files, split them into parameters needed for 
the classes
'''
import classes
grade_file=open('grades.txt','r')
student_file=open('students.txt','r')
grade_file=grade_file.read()
grade_file.split(" ")
student_file=student_file.read()
student_file.split(" ")
num=grade_file[0]
grades=grade_file[2:]
print(grades)
first=student_file[1]
last=student_file[2]
A=classes.Grade()
B=classes.Student()
print(B)