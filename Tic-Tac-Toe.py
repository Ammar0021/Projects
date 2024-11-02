#Tic-Tac-Toe
#Notes:
#Create game board
#Create computer move
#Check for tie
#Check for win 

from random import randint
from time import sleep
import colorama
from colorama import Fore

colorama.init()

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

current_player = "X"
running = True

def display_board():
    print(Fore.CYAN + " " + board[0] + "   |   " + board[1] + "   |   " + board[2])
    print(Fore.CYAN + "      -----------")
    print(Fore.CYAN + " " + board[3] + "   |   " + board[4] + "   |   " + board[5])
    print(Fore.CYAN + "      -----------")
    print(Fore.CYAN + " " + board[6] + "   |   " + board[7] + "   |   " + board[8] + Fore.RESET)

def player_move():
    global current_player
    while True:
        try:
            player_input = int(input(Fore.MAGENTA + "Enter a number 1-9: " + Fore.RESET))  
            if player_input < 1 or player_input > 9:
                raise ValueError(Fore.RED + "Invalid number")
            if board[player_input - 1] != "-":
                raise ValueError(Fore.RED + "Position already taken")
            board[player_input - 1] = current_player
            break
        
        except ValueError as e:
            print(e)

def computer_move():
    print(Fore.YELLOW + "Computer is thinking..." + Fore.RESET)
    sleep(1.5)
    
    move = randint(0, 8)
    while board[move] != "-":
        move = randint(0, 8)
        
    board[move] = "O"
    print(Fore.BLUE + f"Computer chose position {move + 1}")
    sleep(1)

def check_winner():
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            return board[condition[0]]
    return None

def check_draw():
    return "-" not in board

def game_status():
    global running
    game_winner = check_winner()
    
    if game_winner:
        sleep(0.5)
        display_board()
        print(Fore.GREEN + f"{game_winner} wins!" + Fore.RESET)
        running = False
        return True
    
    if check_draw():
        sleep(0.5)
        display_board()
        print(Fore.BLUE + "It's a draw!" + Fore.RESET)
        running = False
        return True
    
    return False

while running:
    display_board()
    player_move()
    
    if game_status():
        break
    
    current_player = "O"
    computer_move()
    display_board()
    
    if game_status():
        break
    
    current_player = "X"


