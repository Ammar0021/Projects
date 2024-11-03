#Tic-Tac-Toe
#Notes:
#Create game board
#Create computer move
#Check for tie
#Check for win 
#Ask user to continue
#Score Tracking


from random import randint
from time import sleep
import colorama
from colorama import Fore, Style

colorama.init()

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

current_player = "X"
running = True

player_score = 0
computer_score = 0
player_wins = 0
computer_wins = 0
draws = 0

def display_board():
    print("\n" + Fore.CYAN + " " + board[0] + "   |   " + board[1] + "   |   " + board[2])
    print(Fore.CYAN + "-------------------")  
    print(Fore.CYAN + " " + board[3] + "   |   " + board[4] + "   |   " + board[5])
    print(Fore.CYAN + "-------------------")  
    print(Fore.CYAN + " " + board[6] + "   |   " + board[7] + "   |   " + board[8] + Fore.RESET + "\n") 


def welcome_page():
    print(Style.BRIGHT + Fore.WHITE + "Welcome to Tic-Tac-Toe!" + Fore.RESET + "\n")
    print(Fore.GREEN + "Winning will give you 1 point." + Fore.RESET)
    print(Fore.YELLOW + "If you tie, you get 0.5 points." + Fore.RESET)
    print(Style.BRIGHT +Fore.RED + "If you lose, you get 0 points." + Fore.RESET) 


welcome_page()
def player_move():
    global current_player
    while True:
        
        try:
            player_input = int(input(Fore.MAGENTA + "Enter a number between 1-9: " + Fore.RESET))  
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
    print(Fore.BLUE + f"Computer chose position {move + 1}" + Fore.RESET)
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
        print(Fore.GREEN + f"{game_winner} wins!" + Fore.RESET + "\n")
        running = False
        
        return True
    
    if check_draw():
        sleep(0.5)
        display_board()
        print(Fore.BLUE + "It's a draw!" + Fore.RESET + "\n")
        running = False
        
        return True
    
    return False

def reset_board():
    global board, current_player
    board = ["-", "-", "-", 
            "-", "-", "-", 
            "-", "-", "-"]

current_player = "X"

def print_scores(player_score, computer_score, player_wins, computer_wins, draws):
    print(f"{Fore.CYAN}Player Score: {player_score}{Fore.RESET} | "
          f"{Fore.GREEN}Player Wins: {player_wins}{Fore.RESET} | "
          f"{Fore.RED}Player Losses: {computer_wins}{Fore.RESET} | "
          f"{Fore.YELLOW}Player Draws: {draws}{Fore.RESET} | \n")

    print(f"{Fore.CYAN}Computer Score: {computer_score}{Fore.RESET} | "
          f"{Fore.GREEN}Computer Wins: {computer_wins}{Fore.RESET} | "
          f"{Fore.RED}Computer Losses: {player_wins}{Fore.RESET} | "
          f"{Fore.YELLOW}Computer Draws: {draws}{Fore.RESET}")



while True:
    reset_board()
    running = True


    while running:
        display_board()
        player_move()

        if game_status():
            if check_winner() == "X":
                player_score += 1
                player_wins += 1


            elif check_draw() == "X":
                player_score += 0.5
                draws += 1
            break

        current_player = "O"
        computer_move()

        if game_status():
            if check_winner() == "O":
                computer_score += 1
                computer_wins += 1

            elif check_draw() == "O":
                computer_score += 0.5
                draws += 1
            break

        current_player = "X"
        

    print_scores(player_score, computer_score, player_wins, computer_wins, draws)
    print()
    
    while True:
        try:
            play_again = input(Fore.MAGENTA + "Do you want to play again? (yes/no): " + Fore.RESET).lower()
            if play_again == "no":
                print(Fore.YELLOW + "Thank you for playing!" + Fore.RESET)
                sleep(1)
                exit()
            
            elif play_again == "yes":
                print("Starting a new game...")
                sleep(2)
                break
                
            else:
                raise ValueError(Fore.RED + "Invalid input. Please enter 'yes' or 'no'." + Fore.RESET)    
        except ValueError as e:
            print(e)
            
