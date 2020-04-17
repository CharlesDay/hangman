import time
import random


def random_word(file_name):
    lines = open(file_name).read().splitlines()
    return random.choice(lines)


name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")

print("")

time.sleep(1)
user_continues = "y"

try:
    while user_continues.lower() == "y":
        print("Start guessing...")
        time.sleep(0.5)
        word_to_guess = ""
        words = int(input("How many words do you want?"))
        my_file = open("words.txt", "rt")
        for _ in range(words):
            word_to_guess += random_word("words.txt") + " "
        word_to_guess = word_to_guess[:-1]
        guesses = ''
        turns = int(input("How many turns do you want?"))
        original_turns = turns

        while turns > 0:
            failed = 0
            for char in word_to_guess:
                if char in guesses:
                    print(char)
                else:
                    print("_")
                    failed += 1
            if failed == 0:
                print("You won!")
                break

            guess = input(str("guess a character:"))
            guesses += guess
            if guess not in word_to_guess:
                turns -= 1
                print("Wrong")
                print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You lose the word was", word_to_guess + "\n")
        turns = original_turns
        user_continues = input(str("Do you want to play again? (y/n)"))
except ValueError:
    print("Please enter valid input")
