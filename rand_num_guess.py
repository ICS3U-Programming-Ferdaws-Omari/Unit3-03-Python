#!/usr/bin/env python3
# Created By: Ferdaws
# Date: April 3, 2022
# This program guesses a number between 1 and 10.
import random


def main():
    hidden = random.randint(1, 10)
    # a number between 1 and 10
    # print hidden

    # input
    guess = int(input("Guess a number between 1 and 10 :"))

# check the numbers is equal to hidden
    if guess == hidden:
        print("you guessed right")

# check the numbers is not equal to hidden
    if guess != hidden:
        print("you guessed wrong")
        print("The correct answer is")
        print(hidden)


if __name__ == "__main__":
    main()
