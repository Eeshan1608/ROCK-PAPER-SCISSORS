
  





#  Objective:
#  Create a Python program where the computer
# randomly selects a number from a list, and the
# player has to guess it.

#  Online research is encouraged (Python
# concepts, Syntax, etc.).
#  Using AI to create the program or certain parts of it
# is not allowed.

# Practice &
# Homework

#  Instructions:
#  Create a list of numbers from 1 to 20.
#  Use the random module to have the computer
# select a random number from this list (see
# https://www.w3schools.com/python/ref_random_r
# andom.asp for reference)
#  Ask the user to input their name and welcome
# them to the game.
#  Prompt the player to guess the number.
#  Provide hints using if-else statements:
#  If the guess is too low, print "Too low! The correct
# number was [number]“
#  If the guess is too high, print "Too high! The correct
# number was [number]“
#  If the guess is correct, print "Congratulations,
# [name]! You've guessed the number!“

import random
guess_number = 0
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
name = input("Enter your name: ")
print ("Hello", name, "welcome to the game")
print("")
print("Please guess a number between 1 and 20")
print("")
while True:
    comp_choice = random.choice(number_list)
    while True:
      guess_number = int(input("Enter your guess: "))
      if guess_number == comp_choice:
        print("Correct")




      elif guess_number < comp_choice:
        print("Too low")
      elif guess_number > comp_choice:
        print("Too high")

      playagain = input("Do you want to play again? (yes/no): ")
      if playagain.lower() == "no":
        break