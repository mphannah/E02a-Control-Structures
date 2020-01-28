#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red' or color == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#This program is trying to allow the user to answer Red or red, which trys to get rid of the problem of case sensitivity
#It end with the program printing "Sorry, try again."