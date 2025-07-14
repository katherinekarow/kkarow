# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:25:40 2016

@author: ferna199
"""

dictionary=open("dictionary.txt",'r')
vowels="aeiouy"
for line in dictionary: 
    line=line.lower()
    words=line
    if "a" in line:
      i = int(words.index('a'))
      
      words=words[i:]
      print(i)
      if "e" in words:
          i = int(words.index('e'))
          words=words[i:]
          if "i" in words:
              i = int(words.index('i'))
              words=words[i:]
              if "o" in words:
                  i = int(words.index('o'))
                  words=words[i:]
                  if "u" in words:
                      i = int(words.index('u'))
                      words=words[i:]
                      print (line)
                      break



vowels=str("aeiouy")

for line in dictionary:
    if line == line.lower():
        if "s" not in line:
            line=line.strip()
            if len(line) == 7: 
                count_vowels=0
                for c in line:
                    if c in vowels:
                        count_vowels+=1
                if count_vowels!=1:
                    continue
                else: 
                    print (line)