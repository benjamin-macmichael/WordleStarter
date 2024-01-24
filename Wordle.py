# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    CORRECT_COLOR = "#66BB66" # A shade of green
    PRESENT_COLOR = "#CCBB66" # A shade of brownish yellow
    MISSING_COLOR = "#999999" # A shade of gray

    # Code that takes a random 5 letter word and places it in the first row of the grid
    random_word = random.choice(FIVE_LETTER_WORDS)
    print(random_word)
    next_row = False

    def enter_action(s):
        global complete # var to see if user has guessed correctly.
        global next_row
        # setting up for after they get the word right so they can't continue typing
        try:
            if complete == True:
                # gw.set_current_row(row)
                pass
        except:
            complete = False
                
        if complete != True:
            row = gw.get_current_row()
            if s.lower() not in FIVE_LETTER_WORDS:
                gw.show_message('Sorry, that is not in our word bank')
                next_row = False # set next row to false bc it is not a correct word
                return
            else:
                next_row = True # set to true for the next row to go. 
            # this logic puts the user on the next row after hitting enter. needs to only happen if they have success
            if next_row and row != N_ROWS - 1:
                gw.set_current_row(row+1)
            
            # sets all keys to green and ends function if they are correct.
            if s.lower() == random_word:
                for i in range(0,5):
                    gw.set_square_color(row, i, CORRECT_COLOR)
                    gw.set_key_color(s[i], CORRECT_COLOR)
                # say congrats since they won!
                gw.show_message('Congrats!')
                complete = True
                return
    
            # divide into two arrays for tracking and setting up for colors.
            guess_array = list(s.lower())
            correct_array = list(random_word)
            color_keys_array = list(s)
            pos = 0
            for i in range(0,5):
                # iterate to 
                if guess_array[i] == correct_array[i]:
                    guess_array[i] = CORRECT_COLOR
                    correct_array[i] = 'correct'
                elif guess_array[i] in correct_array:
                    pos = len(correct_array) - 1 - correct_array[::-1].index(guess_array[i])
                    correct_array[pos] = 'present'
                    guess_array[i] = PRESENT_COLOR
                else:
                    guess_array[i] = MISSING_COLOR
                # set up for coloring the keys
                key_color = gw.get_key_color(color_keys_array[i].upper()) # var to get the key color
                gw.set_square_color(row, i, guess_array[i])
                # iterate through each option to color the keys correctly
                if key_color == MISSING_COLOR or key_color == "#FFFFFF":
                    gw.set_key_color(color_keys_array[i], guess_array[i])
                elif key_color == PRESENT_COLOR:
                    if guess_array[i] == MISSING_COLOR:
                        gw.set_key_color(color_keys_array[i], guess_array[i])
                elif key_color == CORRECT_COLOR:
                    pass
                else:
                    print('Accident')

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
# Startup code
if __name__ == "__main__":
    wordle()
