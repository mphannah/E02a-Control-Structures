#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
count = 0
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    count = count + 1               # You can also write this as count += 1
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')


print('You guessed it in {} tries!'.format(count))

#The count is there to show the user how many times they tried the question. Each time it goes through the loop it adds one to count
#This line tells the user how many tries it took to guess "red"