#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')

#Lines 10-17 are indented because a while loop was added and you have to indent all that you want inside the loop
#That would cause an infinite loop because there is no way to change color so it can never = "red"