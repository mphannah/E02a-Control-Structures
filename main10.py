#!/usr/bin/env python3
import sys, random     #imports sys and random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"    


print('Greetings!')     #prints "Greetings!" to the user
colors = ['red','orange','yellow','green','blue','violet','purple']     #creates a list of colors
play_again = ''     #creates the variable play_again
best_count = sys.maxsize     # the biggest number

while (play_again != 'n' and play_again != 'no'):     #creates a while loop that loops when play_again doesn't = "no" or "n"
    match_color = random.choice(colors)     #creates a variable that picks a random color from the list colors
    count = 0     #creates a variable called count and sets the value to 0
    color = ''     #creates the variable color
    while (color != match_color):     #creates a while loop that loops when color doesn't = match_color
        color = input("\nWhat is my favorite color? ")     #\n is a special code that adds a new line, has the user enter a value for color
        color = color.lower().strip()     #makes every character in color a lowercase and strips the variable of unnecessary spaces
        count += 1     #adds 1 to count every time the loop continues
        if (color == match_color):     #if color is equal to match color it sends the program one line down
            print('Correct!')     #prints "Correct!"
        else:     #if color doesn't = match_color sends the program one line down
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))     
                                                            #prints "Sorry, try again. You have guessed (count) times."
    print('\nYou guessed it in {} tries!'.format(count))     #after color equals match_color this prints the total # of times you guessed

    if (count < best_count):     #if count is less than best_count 
        print('This was your best guess so far!')     #prints "This was your best guess so far!"
        best_count = count     #and changes best_count to your currect count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()     #has the user input if they want to play again it makes every character lowercase
                                                                                           #and strips it of unnecessary spaces, if anything but "n" or "no" it goes back to the first while loop
print('Thanks for playing!')     #if play_again is "n" or "no" program prints this