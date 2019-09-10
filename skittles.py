"""
Tung Hoang - 09/19/19
This program will make the user guess the amount of skittles the candy machine
currently have. The porgram will keep asking until the user guess it right.
"""
import random

# Asking user input
print("Konnichinya~. I'm the ceiling CAT. I'm here to give out free Skittliya~.")
userGuess = int(input("Guess how many Skittles I have nyahaha~~: "))

# Set the random number of candy
numCandy = random.randint(0,1024)

# Checking if the guess is correct, too low or too high and let user guess again
while userGuess != numCandy:
    if userGuess < 0:
        userGuess = int(input("Wait. That's illegal. Try againya~~~ "))
    elif userGuess < numCandy:
        userGuess = int(input("Too looww~. Try againya~~~ "))
    else:
        userGuess = int(input("Too highh~. Try againya~~~ "))

# Print when guess correctly     
print("Yay!!! You guess correctly~. You get to taste the rainbow nYahAHaH~~")
