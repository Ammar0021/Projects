#Hangman

#Notes:
#Random
#List of words
#Print the hangman
#Conditionals
#Count Controlled

import random
from time import sleep

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
    print("***********")
    for line in hangman_art[wrong_guesses]:
        print (line)
    print("***********")
        
        
def display_hint(hint):
    print(" ".join(hint))
    
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] *len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    running = True

    while running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                
            
        
        
        
        
    
main()






    
