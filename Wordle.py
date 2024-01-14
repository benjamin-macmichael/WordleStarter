# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

# This function checks to see if the word the user input is in the 5 letter word dictionary of valid wordle words
    def enter_action(s):

        # initiliaze our variables
        iCount = 1
        new_guess = ''

        #loop that creates the string variable for the user's guess by taking each letter one at a time and appending it to new_guess
        while iCount < 6 :
            new_guess = new_guess + str(gw.get_square_letter(0, iCount - 1))
            if new_guess.lower() not in (FIVE_LETTER_WORDS) :
                gw.show_message("Not in word list.")
            else :
                gw.show_message("Milestone 2 working!")
            iCount += 1

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Code that takes a random 5 letter word and places it in the first row of the grid
    random_word = random.choice(FIVE_LETTER_WORDS)

    for i in range(len(random_word)):
        gw.set_square_letter(0, i, random_word[i])

# Startup code

if __name__ == "__main__":
    wordle()
