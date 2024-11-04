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

colorama.init() # Initialize colorama

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

#Sets the human player to 'X'
current_player = "X"
running = True

player_score = 0
computer_score = 0
player_wins = 0
computer_wins = 0
draws = 0

#display the game board
def display_board():
    
    print("\n" + Fore.CYAN + " " + board[0] + "   |   " + board[1] + "   |   " + board[2])
    print(Fore.CYAN + "-------------------")  
    print(Fore.CYAN + " " + board[3] + "   |   " + board[4] + "   |   " + board[5])
    print(Fore.CYAN + "-------------------")  
    print(Fore.CYAN + " " + board[6] + "   |   " + board[7] + "   |   " + board[8] + Fore.RESET + "\n") 


def welcome_page():
    
    print(Style.BRIGHT + Fore.WHITE + "Welcome to Tic-Tac-Toe!" + Fore.RESET + "\n") #Added extra new line
    sleep(1)
    print(Fore.GREEN + "Winning will give you 1 point." + Fore.RESET)
    sleep(0.35)
    print(Fore.YELLOW + "If you tie, you get 0.5 points." + Fore.RESET)
    sleep(0.35)
    print(Style.BRIGHT +Fore.RED + "If you lose, you get 0 points." + Fore.RESET) 


welcome_page()
def player_move():
    
    global current_player
    while True: #Loop until valid input is provided
        
        try:
            sleep(1.5)
            player_input = int(input(Fore.MAGENTA + "Enter a number between 1-9: " + Fore.RESET))  
            if player_input < 1 or player_input > 9:   
                raise ValueError(Fore.RED + "Invalid number")
            
            if board[player_input - 1] != "-": #Check is position is taken
                raise ValueError(Fore.RED + "Position already taken")
            
            board[player_input - 1] = current_player
            break #Exit the loop if valid input is provided
        
        except ValueError as e:
            print(e) #Print error message and ask for input again

def computer_move():
    print(Fore.YELLOW + "Computer is thinking..." + Fore.RESET)
    sleep(1.5) #Simulate thinking time for computer's move
    
    move = randint(0, 8) #Randomly choose a computer move
    while board[move] != "-": #Ensures position is not taken
        move = randint(0, 8)
        
    board[move] = "O" #Place computer's move in the chosen position
    print(Fore.BLUE + f"Computer chose position {move + 1}" + Fore.RESET)
    sleep(1) #Small delay after computer move

def check_winner():
    
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),  #Rows
                      (0,3,6), (1,4,7), (2,5,8),  #Columns
                      (0,4,8), (2,4,6)]           #Diagonals
    
    for condition in win_conditions:
        
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            return board[condition[0]] #Returns the winner ('X' or 'O')
    return None #Returns None if no winner

def check_draw():
    return "-" not in board #Returns True if all positions are filled

def game_status():
    
    global running
    game_winner = check_winner() #Checks for a winner
    
    if game_winner:
        sleep(0.5)
        display_board() #Displays the final board
        print(Fore.GREEN + f"{game_winner} wins!" + Fore.RESET + "\n")
        running = False
        
        return True
    
    if check_draw():
        sleep(0.5)
        display_board()
        print(Fore.BLUE + "It's a draw!" + Fore.RESET + "\n")
        running = False
        
        return True
    
    return False #Returns False is game is ongoing

def reset_board():
    
    global board, current_player
    board = ["-", "-", "-", 
            "-", "-", "-",    #Resets the board
            "-", "-", "-"]   

current_player = "X"  #Resets current player to 'X'

def print_scores(player_score, computer_score, player_wins, computer_wins, draws):
    
    print(f"{Fore.CYAN}Player Score: {player_score}{Fore.RESET} | "
          f"{Fore.GREEN}Player Wins: {player_wins}{Fore.RESET} | "
          f"{Fore.RED}Player Losses: {computer_wins}{Fore.RESET} | "
          f"{Fore.YELLOW}Player Draws: {draws}{Fore.RESET} | \n")  #Space between scores
    
    

    print(f"{Fore.CYAN}Computer Score: {computer_score}{Fore.RESET} | "
          f"{Fore.GREEN}Computer Wins: {computer_wins}{Fore.RESET} | "
          f"{Fore.RED}Computer Losses: {player_wins}{Fore.RESET} | "
          f"{Fore.YELLOW}Computer Draws: {draws}{Fore.RESET}")



while True:
    reset_board() #reset everything for new game
    running = True


    while running:
        sleep(1.5)
        display_board()
        player_move()

        if game_status(): #check if game has ended after player's move
            if check_winner() == "X": #update  scores for players win
                player_score += 1
                player_wins += 1


            elif check_draw() == "X":
                player_score += 0.5
                draws += 1
            break #breaks inner loop to start a new game

        current_player = "O" #switch to computer's turn after player's move
        computer_move() #Handles computer's move after player's turn

        if game_status():
            if check_winner() == "O":
                computer_score += 1
                computer_wins += 1

            elif check_draw() == "O":
                computer_score += 0.5
                draws += 1
            break

        current_player = "X"
        

    print_scores(player_score, computer_score, player_wins, computer_wins, draws) #prints the stats after game ends
    print() #prints a new line for clear visual
    
    while True:
        
        try:
            play_again = input(Fore.MAGENTA + "Do you want to play again? (yes/no): " + Fore.RESET).lower()
            if play_again == "no":
                print(Fore.YELLOW + "Thank you for playing!" + Fore.RESET)
                sleep(1)
                exit() #exits the game
            
            elif play_again == "yes":
                print("Starting a new game...")
                sleep(2)
                break
                
            else:
               
                raise ValueError(Fore.RED + "Invalid input. Please enter 'yes' or 'no'." + Fore.RESET)    
        except ValueError as e:
            print(e)
            
