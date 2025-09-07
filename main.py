# # import necessary libraries
# #import getpass
# # use getpass for hidden input
# # use getpass for hidden input
# #secret_word = getpass.getpass("Enter your word:").lower()
# #hint = input("Enter a hint: ")
# #guessed_letters = []
# #wrong_guesses = 0
# #max_wrong = 5
# #display = ""

# # fix the error in the condition
# #while wrong_guesses < max_wrong:
#   #  display = ""
#   #  for letter in secret_word:
#    #     if letter in guessed_letters:
#    #         display = display + letter
#   #      else:
#          #   display += "_"

#   #  print("Word:", display)
#     print("Hint:", hint)

#     # fix the condition to check if the word has been guessed
#     if display == secret_word:
#         print("Congratulations! You guessed the word:", secret_word)
#         break
    

#     # convert the input to lowercase
#     guess = input("Enter a letter: ").lower()

#     if guess not in secret_word:
#         # make sure a life is lost if the guessed letter is not in the word
#         wrong_guesses = wrong_guesses  + 1
#         print("Wrong guess! Lives left:", max_wrong - wrong_guesses)
#         guessed_letters.append(guess)
#         print(guessed_letters)

#     else:
#         print ("Correct guess!")
#         guessed_letters.append(guess)
#         print(guessed_letters)

# if display != secret_word:
#     print("Game over! The word was: ", secret_word)

# print("")
# while True:
#     print ("Do you want to play again?")
#     playagain = input("If you want play again type yes or no: ").lower()
#     if playagain == "yes":
#         continue 
#     else:
#         break 




# import random
# user_choice = 0
# user_wins = 0
# gestures = ["rock", "scissor","paper"]
# options = [1,2,3]
# print ("Hello welcome to ROCK SCISSOR PAPER GAME DO YOU KNOW THE RULES? Rock = 1, Scissor = 2, Paper = 3 ")
# print("")
# rules = input("If you don't know the rules type no if you know the rules type yes: ")
# if rules.lower == "no":
#     print("Rock beats scissor, scissor beats paper, and paper beats rock")
#     print("")
#     print("Rock = 1, Scissor = 2, Paper = 3")
#     print("we play now")
# else:
#     print("ok we play now")

# while True:
#     user_choice = int(input("Enter your choice: "))
    
#     comp_choice = random.choice(options)
#     print("Computer choice is: ",(gestures[comp_choice - 1]))
#     if user_choice - comp_choice == -1 or user_choice - comp_choice == 2:
#         print("You win")
#         user_wins += 1
#         print("Your score is: ", user_wins)
#     elif user_choice == comp_choice:
#         print("It's a tie")
#         user_wins += 0
#         print("your score is: ", user_wins)
        
#     else:
#         print("you lost")
#         user_wins -= 1
#         print("your score is: ", user_wins)

    

#     playagain = input("Do you want to play again? (yes/no): ")
#     if playagain.lower() == "no":
#         print("Your final score is: ", user_wins)
#         break
    

        

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
    
    
number_list: list[int] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
