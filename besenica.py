import random


def play_hangman():
    word_list = ['apple','banana','orange','strawberry','kiwi','cherry','nectarine','watermelon','melon','pineapple','mango','lemon','grapefruit','blueberry','raspberry','avocado','grapes','pear','pomegranate']
    word = random.choice(word_list)
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))
    print("_ " * len(word))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed that letter. Try again")
            continue

        if guess.isalpha() and len(guess) == 1:
            guessed_letters.append(guess)

            if guess in word:
                progress = ""
                for letter in word:
                    if letter in guessed_letters:
                        progress += letter + " "
                    else:
                        progress += "_ "
                print(progress)

                if "_" not in progress:
                    print("Congratulations! You guessed it")
                    break
            else:
                wrong_guesses += 1
                print("Wrong! Remaining attempts: {}.".format(6 - wrong_guesses))

                if wrong_guesses == 6:
                    print("You lost. The word was:  '{}'.".format(word))
                    break
        else:
            print("Only one letter bro.")

play_hangman()
play_again = input("Do you wish to play? (yes/no): ").lower()
while play_again == "yes":
    if play_again == "yes":
        play_hangman()
        play_again = input("Do you wish to play? (yes/no): ").lower()
if play_again == "no":
    print("Thanks for playing!")
else:
    print("That is not play again")