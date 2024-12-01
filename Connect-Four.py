#Connect Four
#Notes:
#Define game board (6 Rows, 7 Columns)
#42 total discs
#2 Players or 1 Player (vs Computer)
#Placing a piece
#winning conditions
#Game loop
#Computer Difficulty
#Update main()


import colorama
import os
import sys
import random
from random import randint
from time import sleep
from colorama import Fore, Style
from collections import deque, defaultdict


colorama.init(autoreset=True)
colours = [Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX,Fore.LIGHTYELLOW_EX, Fore.YELLOW]

RED_DISC = Fore.RED + "O"
YELLOW_DISC = Fore.YELLOW + "O"

# this is for compatibility
def clear_screen():  
    
    if sys.platform == 'darwin' or sys.platform == 'linux':  # MacOS or Linux
        os.system('clear')  
    elif sys.platform == 'win32':  # Windows
        os.system('cls') 

def welcome_screen():
    clear_screen()
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to Connect Four!")
    sleep(0.75)
    
def game_mode():
    while True:
        try:
            sleep(0.4)
            print(Fore.CYAN + "Choose Your Game Mode!\n")
            sleep(0.8)
            print(Fore.LIGHTYELLOW_EX + "1. Single Player (Vs Computer)")
            sleep(0.4)
            print(Fore.LIGHTMAGENTA_EX + "2. Two Player Mode\n")
            sleep(1)
            choice = input(Fore.LIGHTWHITE_EX + "Enter 1 or 2: ").strip()
            print()
            clear_screen()
            
            if choice == "1":
                print(Fore.LIGHTYELLOW_EX + "Starting Single Player Mode!\n")
                sleep(0.7)
                difficulty = choose_difficulty()
                print()
                return "single", difficulty  # Stores "single" in "mode" 
            
            elif choice == "2":
                print(Fore.LIGHTMAGENTA_EX + "Starting Two Player Mode!") 
                sleep(0.7)
                print()
                return "multi", None  # Stores "multi" in "mode",  None is for No Difficulty
             
            else:
                raise ValueError(Fore.LIGHTRED_EX + "Invalid choice! Please enter 1 or 2 only.") 
        except ValueError as error:
            print(error)             
    
def initialise_board():
    return [deque([' '] * 6) for i in range(7)]  # 6 rows, 7 columns

def display_board(board):
    clear_screen()

    for row in range(6):  
        row_string = ""
        
        for col in range(7):
            row_string += Fore.CYAN + "| " + board[col][row] + " "  # Add each disc with a Cyan column separator
        row_string += "|"
        print(row_string)  # Print the full row
        print(Fore.GREEN + "------------------------------" + Fore.RESET)  # Print the row separator in Green



def winning_conditions():
    win_conditions = []

    # Horizontal Conditions
    for row in range(6):             #Iterates over each row
        for col in range(4):         #Iterates over each column
            
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
    for condition in win_conditions:                                        # Iterates over each winning condition
        if all(board[col][row] == player for row, col in condition):        # Checks if winning conditions are filled
            return True  
    return False  

def player_move(board, player):
    while True:
        try:
            print()
            sleep(0.3)
            col = int(input(random.choice(colours) + Style.BRIGHT + "Choose a Column (1-7): " + Style.RESET_ALL).strip()) - 1  # -1 due to 0 indexing
            if col < 0 or col > 6:
                raise ValueError(Fore.LIGHTRED_EX + "Invalid Choice!, Please choose between 1 and 7, only")

            if board[col][0] != ' ':
                raise ValueError(Fore.LIGHTRED_EX + "Column is full, Please choose another column")
            
            for row in reversed(range(6)):
                if board[col][row] == ' ':
                    board[col][row] = player
                    return   #Ends move, returns control to game loop
                
        except ValueError as error:
            print (error)

def computer_easy(board, computer):
    while True:
        col = randint(0, 6)
        if board[col][0] == ' ':
            for row in reversed(range(6)):
                if board[col][row] == ' ':
                    board[col][row] = computer
                    print("Computer is thinking...")
                    sleep(0.9)
                    print()
                    print(f"{Fore.LIGHTGREEN_EX}Computer placed disc in column {col + 1}")
                    sleep(0.9)
                    return
                
def computer_medium(board, computer, player):
    #Blocking the Player's Winning Move    
    for col in range (7):
        if board[col][0] == ' ':            
            for row in reversed(range(6)):
                if board[col][row] == ' ':
                    board[col][row] = player 
                    if check_win(board, winning_conditions(), player):   # If player is winning, Computer will Block the move
                        board[col][row] = computer 
                        print(f"{Fore.LIGHTYELLOW_EX}COmputer placed disc in column {col + 1}")
                        sleep(0.9)
                        return
                    board[col][row] = ' '   #this undoes the move if it didn't Block
    
    computer_easy(board, computer)  # Reverts to Easy Mode if no Win or Block found
    
def computer_hard(board, computer, player):
    # Logic for trying to win
    for col in range(7):
        if board[col][0] == ' ':  # Check if column is not full
            for row in reversed(range(6)):
                if board[col][row] == ' ':
                    board[col][row] = computer
                    if check_win(board, winning_conditions(), computer):  # If Computer will Win, it will play this move
                        print(f"{Fore.YELLOW}Computer placed disc in column {col + 1}")
                        sleep(0.9)
                        return
                    board[col][row] = ' '  #this undoes the move if it didn't Block

    # If there is no winning move, Computer will Block
    for col in range(7):
        if board[col][0] == ' ': 
            for row in reversed(range(6)):
                if board[col][row] == ' ':
                    board[col][row] = player
                    if check_win(board, winning_conditions(), player): 
                        board[col][row] = computer
                        print(f"{Fore.YELLOW}Computer placed disc in column {col + 1}")
                        sleep(0.9)
                        return
                    board[col][row] = ' '  

    computer_easy(board, computer)  


def choose_difficulty():
    while True:
        try:
            print(Fore.LIGHTMAGENTA_EX + "Select Difficulty:\n")
            print(Fore.GREEN + "1. Easy")
            print(Fore.YELLOW + "2. Medium")
            print(Fore.RED + Style.BRIGHT + "3. Hard\n")
            
            difficulty = input("Enter 1,2 or 3: ").strip()
            
            if difficulty == "1":
                print(Fore.GREEN + "You have selected Easy Mode")
                sleep(0.5)
                return "easy"  #Stores 'easy' in difficulty
            
            elif difficulty == "2":
                print(Fore.YELLOW + "You have selected Medium Mode")
                sleep(0.5)
                return "medium"
            
            elif difficulty == "3":
                print(Fore.RED + "You have selected Hard Mode!")
                sleep(0.5)
                return 'hard'
            
            else:
                raise ValueError(Fore.LIGHTRED_EX + "Invalid Choice! Please enter 1,2 or 3 only.")
        except ValueError as error:
            print(error)
            
            
                         
            
def disc_colour(mode):
    if mode == "multi":
        while True:
            try:
                clear_screen()
                print(Fore.LIGHTYELLOW_EX + "Choose Your " + Fore.LIGHTRED_EX + "Disc Colour!\n")
                print(Fore.RED + "1. Red (🔴)")
                print(Fore.YELLOW + "2. Yellow (🟡)\n")
                disc_colour = int(input("Enter 1 or 2: ").strip())
                
                if disc_colour == 1:
                    player1 = RED_DISC
                    player2 = YELLOW_DISC
                    sleep(0.5)
                    break #exits loop
                
                elif disc_colour == 2:
                    player1 = YELLOW_DISC
                    player2 = RED_DISC
                    sleep(0.5)
                    break
                
                else:
                    raise ValueError(Fore.LIGHTRED_EX + "Invalid Choice, Please Choose 1 or 2 Only")
            except ValueError as error:
                print(error)
        return player1, player2  # Returns disc colour for both players
                
    elif mode == "single":
        while True:
            try:
                print(Fore.LIGHTYELLOW_EX + "Choose Your " + Fore.LIGHTRED_EX + "Disc Colour!\n")
                print(Fore.RED + "1. Red (🔴)")
                print(Fore.YELLOW + "2. Yellow (🟡)\n")
                disc_colour = int(input("Enter 1 or 2: ").strip())
                
                if disc_colour == 1:
                    player = RED_DISC
                    computer = YELLOW_DISC
                    break
                
                elif disc_colour == 2:
                    player = YELLOW_DISC
                    computer = RED_DISC
                    break
                
                else:
                    raise ValueError(Fore.LIGHTRED_EX + "Invalid Choice, Please Choose 1 or 2 Only")
            except ValueError as error:
                print(error)
        return player, computer


def game_loop(board, win_conditions, mode, difficulty):     # This is the heart of the code
    if mode == "multi":
        player1, player2 = disc_colour(mode)  # Gets disc colour for both players
        current_player = player1
    elif mode == "single":
        player, computer = disc_colour(mode)
        current_player = player

    moves_counter = defaultdict(int)  # Counts total moves made
    turn_counter = defaultdict(int)   # This will count how many turns have passed
    
    while moves_counter['total'] < 42:  # 42 is the max moves (7 x 6 =42)
        display_board(board)
        
        # Increment the turn counter
        turn_counter['turn'] += 1
        
        # Display the current turn
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f"Turn {turn_counter['turn']}")
        print()

        if mode == "multi":
            if current_player == player1:
                sleep(0.3)
                print(Fore.RED + "(🔴) It's Player 1's turn!" if player1 == RED_DISC else Fore.YELLOW + "(🟡) It's Player 1's turn!")
                sleep(0.5)
                player_move(board, player1)  # Player 1 makes a move
                
            elif current_player == player2:
                sleep(0.3)
                print(Fore.RED + "(🔴) It's Player 2's turn!" if player2 == RED_DISC else Fore.YELLOW + "(🟡) It's Player 2's turn!") 
                sleep(0.5)
                player_move(board, player2)  
        
        elif mode == "single":
            if current_player == player:
                sleep(0.3)
                print(Fore.RED + "(🔴) It's Your turn!" if player == RED_DISC else Fore.YELLOW + "(🟡) It's Your turn!")
                sleep(0.5)
                player_move(board, player)
                
            elif current_player == computer:
                sleep(0.3)
                print("Computer's turn...")
                sleep(0.9)
                
                if difficulty == "easy":
                    computer_easy(board, computer)
                elif difficulty == "medium":
                    computer_medium(board, computer, player)
                elif difficulty == "hard":
                    computer_hard(board, computer, player)
                
        moves_counter['total'] += 1
                
        if check_win(board, win_conditions, current_player):    # Checks if current player has won
            display_board(board)  
            if mode == "multi":
                if current_player == player1:
                    winner = "Player 1"
                elif current_player == player2:
                    winner = "Player 2"
            elif mode == "single":
                if current_player == player:
                    winner = "You"
                elif current_player == computer:
                    winner = "Computer"

            if winner == "You":
                print(Fore.LIGHTGREEN_EX + f"{winner} win!")  # Grammar handling
            else:
                print(Fore.LIGHTGREEN_EX + f"{winner} wins!")
            break
            
        if mode == "multi":
            if current_player == player1:
                current_player = player2  # This is to switch players
            elif current_player == player2:
                current_player = player1
            
        elif mode == "single":
            if current_player == player:
                current_player = computer
            elif current_player == computer:
                current_player = player
                
    if moves_counter['total'] == 42 and not check_win(board, win_conditions, current_player):    # If board is full and no winner
        display_board(board)
        print(Fore.LIGHTCYAN_EX + "It's a Draw!")
    
    while True:
        try:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                main()  # Restarts the game
            elif play_again == "no":
                sleep(0.5)
                print("\n" + Fore.LIGHTCYAN_EX + "Thanks for playing!")
                sys.exit()# Exits the game
                
            else:
                raise ValueError(Fore.LIGHTRED_EX + "Invalid input! Please enter 'yes' or 'no' only.")
        except ValueError as error:
            print(error)



def main():        
    welcome_screen()      
    board = initialise_board()
    display_board(board)
    
    mode, difficulty = game_mode()
    if mode == "single":
        difficulty = choose_difficulty
    else:
        difficulty = None   #This is for Multiplayer mode (which has no Difficulty, obviously)
        
    win_conditions = winning_conditions()
    game_loop(board, win_conditions, mode, difficulty)
 
 

#Checks if script is being run directly, and not imported as a module
if __name__ == "__main__":
    main()



