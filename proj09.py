# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:57:43 2016

@author: KFernandez
"""
'''
import the string so the punctuation can be removed from 
the list of words. Open and read the filewith the open_file 
function
'''
#use try except method to open file
import string
def open_file():
    while True:
        try:
            user_input=(input("Please enter a text file: "))
            fd=open(user_input,"r")
            break
        except IOError:
            print("Oops!  Wrong text file. Try again")
    return fd
fd=open_file()
'''
the fill_completions function returns a dictionary with keys that 
represent the index of the prefix entered
'''
#make the dictionary while using a set so theres no repeated words
def fill_completions(fd):
    c_dict={}
    dict_word=set()
#    words=()
    for line in fd:
        for word in line.strip(string.punctuation).split():
            for i in range(len(word)):
                if word.isalpha() and len(word) > 1:
                    dict_word=word[i]
                    num=word
                    L= (i,dict_word)
                    if L in c_dict:
                        c_dict[L]=num
                    elif L not in c_dict:
                        c_dict[L] = num
    return c_dict
prefix=""
c_dict=fill_completions(fd)
'''
find_completions prints the words that satisfy the conditions 
given by the input
'''
#call the fill_completions function and print out the words
#that satisfy the prefix inputted, break with the pound key
def find_completions(prefix, c_dict):
    yes=True
    while yes==True:
        prefix = input("Enter the prefix to complete (Break with #): ")
        search_words = fill_completions(fd)
        print("Completions of {}:".format(prefix),end = '')
        for a in search_words:
            print(a,end = '')
        print()
        for a in search_words:
            print("Completions of {}:".format(prefix),a)
        if prefix == "#":
            yes=False
            break
L=find_completions(prefix, c_dict)