# Rock Paper Scissors:

# Notes:
# 2 players
# Define the options
# 2nd player has random output
# ask 1st player for input
# Robust
# if statements for winning
# Loops
# Counters


import random

options = ("rock", "paper", "scissors")

Player = None
Computer = random.choice(options)
Playing = True
Wins = 0
Losses = 0
Draws = 0

while Playing:

    Player = None
    Computer = random.choice(options) #Added the variables again so it can reset after every iteration
    
    while Player not in options:
        try:
            Player = input("Enter Rock, Paper, or Scissors: ").lower()
            if Player not in options:
                raise ValueError("Please select a choice only from the options")
        except ValueError as ve:
            print(ve)  # This will print the error message


    print(f"Player chose {Player}")
    print(f"Computer chose {Computer}")


    if Player == Computer:
        print("It's a tie, try again")
        Draws += 1

    elif Player == "rock" and Computer == "scissors":
        print("You Win")
        Wins += 1

    elif Player == "paper" and Computer == "rock":
        print("You Win")
        Wins += 1 

    elif Player == "scissors" and Computer == "paper":
        print("You Win")
        Wins += 1 

    else:
        print("You Lose")
        Losses += 1

    playAgain = input("Play Again? (yes/no): ").lower()
    
    while playAgain not in ["yes", "no"]:  
        print("Please enter 'yes' or 'no' only.")
        playAgain = input("Play Again? (yes/no): ").lower()


    if playAgain == "yes":
        Playing = True
        
    else:
      Playing = False #Breaks the loop
            


print("Thanks for playing")
print(f"You won {Wins} {'time' if Wins == 1 else 'times'}.") #Added extra for grammatical error
print(f"You lost {Losses} {'time' if Losses == 1 else 'times'}.")
print(f"You drew {Draws} {'time' if Draws == 1 else 'times'}.")


    

    






