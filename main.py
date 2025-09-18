



import getpass
import random
rules = ""
user_choice = 0
user_choice2 = 0
user_wins2 = 0
user_wins = 0
gestures = ["rock", "scissor","paper"]
options = [1,2,3]
print("Hello welcome to ROCK SCISSOR PAPER GAME R = 1, S = 2, P = 3") 
comp_player = input("Press 1 to play with computer or 2 to play with another player: ")
rules = input("If you don't know the rules type no if you know the rules type yes: ")
if rules.lower() == "no":
    print("Rock beats scissor, scissor beats paper, and paper beats rock")
    print("")
    print("Rock = 1, Scissor = 2, Paper = 3")
    print("we play now")
else:
    print("ok we play now")
if int(comp_player) == 1:
    print("ok we play with computer")
    print("")
    

    while True:
        user_choice = int(input("Enter your choice: "))

        comp_choice = random.choice(options)
        print("Computer choice is: ",(gestures[comp_choice - 1]))
        if user_choice - comp_choice == -1 or user_choice - comp_choice == 2:
            print("You win")
            user_wins += 1
            print("Your score is: ", user_wins)
        elif user_choice == comp_choice:
            print("It's a tie")
            user_wins += 0
            print("your score is: ", user_wins)

        else:
            print("you lost")
            user_wins -= 1
            print("your score is: ", user_wins)



        playagain = input("Do you want to play again? (yes/no): ")
        if playagain.lower() == "no":
            print("Your final score is: ", user_wins)
            break
else:
    
    if rules.lower == "no":
        print("Rock beats scissor, scissor beats paper, and paper beats rock")
        print("")
        print("Rock = 1, Scissor = 2, Paper = 3")
        print("we play now")
    else:
        print("ok we play now")
    while True:
        user_choice = int(getpass.getpass("Enter your choice player1: "))
        user_choice2 = int(getpass.getpass("Enter your choice player 2: "))
        if user_choice - user_choice2 == -1 or user_choice - user_choice2 ==2:
            print("player 1 wins")
            user_wins += 1
            print("Player 1 score is: ", user_wins)
            print("Player 2 score is: ", user_wins2)
        elif user_choice == user_choice2:
            print("ITS TIE")
            user_wins += 0
            user_wins2 += 0
            print("Player 1 score is: ", user_wins)
            print("Player 2 score is: ", user_wins2)
        else:
            print("Player 2 wins")
            user_wins2 += 1
            print("Player 2 score is: ", user_wins2)
            print("Player 1 score is: ", user_wins)

        playagain = input("Do you want to play again? (yes/no): ")
        if playagain.lower() == "no":
            print("Your final score Player 1 is: ", user_wins)
            print("Your final score is Player 2 is: ", user_wins2)
            break
        
            
    
    















