#Connect Four
#Notes:
#Define game board (6 Rows, 7 Columns)
#42 total discs
#2 Players or 1 Player (vs Computer)
#Placing a piece
#winning conditions
#Game loop

import colorama
import os
import sys
from random import randint
from time import sleep
from colorama import Fore, Style
from collections import deque, defaultdict


colorama.init()

def clear_screen():  # This is to make clear_screen() work on all Operating Systems
    
    if sys.platform == 'darwin' or sys.platform == 'linux':  # MacOS or Linux
        os.system('clear')  # Removes any previous clutter in console
    elif sys.platform == 'win32':  # Windows
        os.system('cls') 

def welcome_screen():
    clear_screen()
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to Connect Four!" + Fore.RESET)
    sleep(0.75)
    
def game_mode():
    while True:
        try:
            print(Fore.CYAN + "Choose Your Game Mode!" + Fore.RESET)
            print("1. Single Player (Vs Computer)")
            print("2. Two Player Mode")
            choice = input("Enter 1 or 2: ")
            
            if choice == "1":
                print("Starting Single Player Mode!")
                sleep(0.7)
                return "single"
            
            elif choice == "2":
                print("Starting Two Player Mode!") 
                sleep(0.7)
                return "multi"
             
            else:
                raise ValueError("Invalid choice! Please enter 1 or 2 only.") 
        except ValueError as error:
            print (str(error))             
    
def initialise_board():
    return [[' ' for _ in range(7)] for _ in range(6)]


def display_board(board):
    clear_screen()
    
    for row in board:
        print(Fore.CYAN + "| " + " | ".join(row) + " |")
        print(Fore.GREEN + "------------------------------" + Fore.RESET)
        
welcome_screen()        
board = initialise_board()
display_board(board)
mode = game_mode()







