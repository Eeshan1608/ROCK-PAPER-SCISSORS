




import random
user_choice = 0
user_wins = 0
gestures = ["rock", "scissor","paper"]
options = [1,2,3]
print ("Hello welcome to ROCK SCISSOR PAPER GAME DO YOU KNOW THE RULES? Rock = 1, Scissor = 2, Paper = 3 ")
print("")
rules = input("If you don't know the rules type no if you know the rules type yes: ")
if rules.lower == "no":
    print("Rock beats scissor, scissor beats paper, and paper beats rock")
    print("")
    print("Rock = 1, Scissor = 2, Paper = 3")
    print("we play now")
else:
    print("ok we play now")

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
    

        

  



