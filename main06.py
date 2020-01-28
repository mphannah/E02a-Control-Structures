#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#I would guess that .strip() is stripping red from any addition spaces that are unnecesarry 
#There wasn't any way I could write red that resulted in the program printing "Sorry, try again."