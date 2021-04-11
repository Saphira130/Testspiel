#!/usr/bin/env python3

import random

my_number = random.randrange(0, 100, 1)

print("I thought of a number between 0 and 100. Can you guess it?")

while True:
    try:
        guessed_number = int(input())
        
    except ValueError:
        print("Your input has to be a whole number.")
    
    else:
        if guessed_number < my_number:
            print("My number is bigger.")
        elif guessed_number > my_number:
            print("My number is smaller.")
        else:
            break

print("Congratulations! You did it!")
