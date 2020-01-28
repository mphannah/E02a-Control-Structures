#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#The program wants you to answer Red, so it will say "Correct" if you type Red. If it is anything else it will say "Sorry, try again."
#Lines 10 and 12 are indented because after an if else statement you must indent
#If you do not capitalize Red it will print "Sorry, try again."
#This means that color is case sensitive