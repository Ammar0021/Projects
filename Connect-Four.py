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
                return "single" # Stores "single"in "mode"
            
            elif choice == "2":
                print("Starting Two Player Mode!") 
                sleep(0.7)
                return "multi" # Stores "multi"in "mode"
             
            else:
                raise ValueError("Invalid choice! Please enter 1 or 2 only.") 
        except ValueError as error:
            print(error)             
    
def initialise_board():
    return [[' ' for i in range(7)] for i in range(6)]


def display_board(board):
    clear_screen()

#def player_move():


    for row in board:
        print(Fore.CYAN + "| " + " | ".join(row) + " |")
        print(Fore.GREEN + "------------------------------" + Fore.RESET)

def winning_conditions():
    win_conditions = []

    # Horizonal Conditions
    for row in range(6):
        for col in range(4):
            win_conditions.append([(row, col), (row, col +1), (row, col +2), (row, col +3)])
    
    # Vertical Conditions
    for row in range(3):
        for col in range(7):
            win_conditions.append([(row, col), (row +1, col), (row +2, col), (row +3, col)])
    
    # Diagonal Conditions (Up Right)(Bottom Right to Top Left)
    for row in range(3):
        for col in range(4):
            win_conditions.append([(row, col), (row + 1, col +1), (row +2, col +2), (row +3, col +3)])
    
    # Diagonal Conditions (Up Left)(Bottom Left to Top Right)
    for row in range(3):
        for col in range(3, 7):
            win_conditions.append([(row, col), (row + 1, col -1), (row +2, col -2), (row + 3, col -3)])

    return win_conditions        
            
def check_win(board, win_conditions, player):
    for condition in win_conditions:
        if all(board[row][col] == player for row, col in condition):
            return True  
    return False  
    
def main():        
    welcome_screen()        
    board = initialise_board()
    display_board(board)
    mode = game_mode()
    win_conditions = winning_conditions()

if __name__ == "__main__":
    main()







