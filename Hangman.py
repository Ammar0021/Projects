#Hangman

#Notes:
#Random
#List of words
#Print the hangman
#Conditionals
#Count Controlled

import random

words = ("apple","orange","bannana","pineapple","mango")

hangman_art = {0:("  ",
                  "  ",
                  "  "),
               
               1:(" o ",
                  "  ",
                  "  "),
               
               2:(" o ",
                  " ┃ ",
                  "  "),
               
               3:(" o ",
                  "/┃  ",
                  "  "),
               
               4:(" o ",
                  "/┃\\  ",
                  "  "),
               
               5:(" o ",
                  "/┃\\ ",
                  "/  "),
               
               6:(" o ",
                  "/┃\\ ",
                  "/ \\")}



def display_man(wrong_guesses):
    pass

def hint(hint):
    
def answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] *len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    running = True
    
main()



    
