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




import random
user_choice = 0
options = [1,2,3]
print ("Hello welcome to ROCK SCISSOR PAPER GAME DO YOU KNOW THE RULES?")
print("")
rules = input("If you don't know the rules type no if you know the rules type yes: ")
if rules == "no":
    print("Rock beats scissor, scissor beats paper, and paper beats rock")
    print("")
    print("Rock = 1, Scissor = 2, Paper = 3")
    print("we play now")
else:
    print("ok we play now")

while True:
    user_choice = int(input("Enter your choice: "))
    comp_choice = random.choice(options)
    if user_choice == comp_choice:
        print("its a tie!!!")
    else:
        user_choice = 1 and comp_choice == 2
        print("you win")
        user_choice = 1 and comp_choice == 3
        print("you lose")
        user_choice = 2 and comp_choice == 1
        print("you lose")
        user_choice = 2 and comp_choice == 3
        print("you win")
        user_choice = 3 and comp_choice == 1
        print("you win")
        user_choice = 3 and comp_choice == 2
        print("you lose")
        print("")
        




    
    

