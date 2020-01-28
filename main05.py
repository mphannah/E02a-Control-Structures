#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#color.lower() converts every character in the string to a lowercase letter. This allows the user to enter red any way 
# they want and it will still print "Correct"
#It prints "Sorry, try again."