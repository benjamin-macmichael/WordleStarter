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
    # random_word = random.choice(FIVE_LETTER_WORDS)
    random_word = 'hello'
    
    def enter_action(s):
        # initiliaze rowCount for rows, col_count for columns
        col_count = 0
        row = gw.get_current_row()
        # this logic puts the user on the next row after hitting enter. needs to only happen if they have success
        if gw.get_square_color(row,4) != None and row != 5:
            gw.set_current_row(row+1)
        # sets all keys to green and ends function if they are correct.
        if s.lower() == random_word:
            for i in range(0,5):
                gw.set_square_color(row, i, CORRECT_COLOR)
                gw.set_key_color(s[i], CORRECT_COLOR)

            return


        #loop that creates the string variable for the user's guess by taking each letter one at a time and appending it to new_guess
        while col_count <= 4 :
            if s.lower() not in FIVE_LETTER_WORDS:
                gw.show_message('Sorry, that is not in our word bank')
                break  
            if s.lower()[col_count] != random_word[col_count] and s.lower()[col_count] in random_word:
                gw.set_square_color(row, col_count, PRESENT_COLOR) 
                gw.set_key_color(s[col_count], PRESENT_COLOR)

            elif s.lower()[col_count] != random_word[col_count]: 
                gw.set_square_color(row, col_count, MISSING_COLOR) 
                gw.set_key_color(s[col_count], MISSING_COLOR)

            elif s.lower()[col_count] == random_word[col_count]:
                gw.set_square_color(row, col_count, CORRECT_COLOR)
                gw.set_key_color(s[col_count], CORRECT_COLOR)

            else:
                gw.set_square_color(row, col_count, MISSING_COLOR) 
                gw.set_key_color(s[col_count], MISSING_COLOR)

            col_count += 1
            
                
        if s.lower() == random_word:
            gw.show_message('Congrats!')
            return 

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
# Startup code
if __name__ == "__main__":
    wordle()
