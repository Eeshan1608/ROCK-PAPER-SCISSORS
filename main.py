# import necessary libraries
import getpass
# use getpass for hidden input
secret_word = getpass.getpass("Enter your word:").lower()
hint = input("Enter a hint: ")
guessed_letters = []
wrong_guesses = 0
max_wrong = 6
display = ""

# fix the error in the condition
while wrong_guesses < max_wrong:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter
        else:
            display += "_"

    print("Word:", display)
    print("Hint:", hint)

    # fix the condition to check if the word has been guessed
    if display != secret_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

    # convert the input to lowercase
    guess = input("Enter a letter: ").lower()

    if guess not in secret_word:
        # make sure a life is lost if the guessed letter is not in the word
        print("Wrong guess! Lives left:", max_wrong)

if display != secret_word:
    print("Game over! The word was:", secret_word)