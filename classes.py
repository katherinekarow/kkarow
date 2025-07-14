# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:47:06 2016

"""

########################################################
#
# Compter PRoject 11
#
#Create class averages for students on given grades
#
#######################################################

class Grade( object ):


    def __init__( self, assignment='', grades=0, weight=0):
        
        """ Define the parameters"""
            
        self.assignment = assignment
        self.grades   = grades
        self.weight  = weight


    def __str__( self ):

        """ Return a string with the assignment name, grade and weight """

        return "{}    {}    {}".\
            format(self.assignment, self.grades, self.weight)
            
    def __repr__(self):
        return self.__str__()
        
        
class Student( object ):
    def __init__( self, first='', last='', num=0, grades=0):
        
        """ Create lists for the names of students and their grades """
            
        self.first = first
        self.last  = last
        self.id = num
        self.grades = grades

    def add_grade( self, grades):

        """ Create the list of grades """
               
        self.grades.append(grades)            
            
    def calculate_grade( self ):

        """ Calculate the total grade for each student. """
        tot_grade=0
        for grad in self.grades:
            tot_grade+=grad.grades*grad.weight
        return tot_grade

    def __str__( self ):
        """ Return a string that displays the name of the student, 
        their grade and their grade. """
        students_str="{} {}". format(self.first, self.last)
        for item in self.grades:
            students_str+=item.__str__()
        return students_str
        
    def __repr__(self):
        ''' call the string function '''
        return self.__str__()
    ''' The Next four functions are to compare the student averages'''
    def __gt__( self, other ):
        self.calculate_grade>other.calculate_grade
        
    def __lt__( self, other ):
        self.calculate_grade<other.calculate_grade
        
    def __eq__( self, other ):
        if abs(self.calculate_grade-other.calculate_grade) < 10**-6:
            (self.calculate_grade)==(other.calculate_grade)
            return True