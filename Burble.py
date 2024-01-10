# test
# File: Burble.py

"""
This module is not the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.set_square_color(0,0,'#66BB66') # green
        gw.set_square_color(0,1,"#CCBB66") # yellow
        gw.set_square_color(0,2,"#999999") # gray
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Code that takes a random 5 letter word and places it in the first row of the grid
    random_word = random.choice(FIVE_LETTER_WORDS)

    for i in range(len(random_word)):
        gw.set_square_letter(0, i, random_word[i])

# Startup code

if __name__ == "__main__":
    wordle()
