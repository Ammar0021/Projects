import random
from time import sleep

words = (
    "apple", "orange", "banana", "pineapple", "mango",
    "grape", "strawberry", "blueberry", "kiwi", "peach",
    "plum", "coconut", "papaya", "pear", "apricot",
    "watermelon", "pomegranate", "blackberry", "raspberry", "lime",
    "lemon", "cherry", "fig", "date", "guava",
    "nectarine", "tangerine", "cranberry", "persimmon", "cantaloupe"
)


hangman_art = {
    0: ("  ",
        "  ",
        "  "),
    
    1: (" o ",
        "  ",
        "  "),
    
    2: (" o ",
        " ┃ ",
        "  "),
    
    3: (" o ",
        "/┃  ",
        "  "),
    
    4: (" o ",
        "/┃\\  ",
        "  "),
    
    5: (" o ",
        "/┃\\ ",
        "/  "),
    
    6: (" o ",
        "/┃\\ ",
        "/ \\")
}

def display_man(wrong_guesses):
    print("***********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***********")
               
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    running = True

    while running:
        display_man(wrong_guesses)
        display_hint(hint)
        
        try:
            guess = input("Enter a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Invalid Input")
        except ValueError as ve:
            print(ve)
            continue  # Skip to the next iteration of the loop
            
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue  # Skip the rest of the loop if the letter has been guessed
        
        guessed_letters.add(guess)  # Add guess to the set of guessed letters
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            
            if "_" not in hint:
                print(f"Congratulations! You've guessed the word: {answer}")
                running = False  # End the game since the player has won
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} guesses left.")
            
            if wrong_guesses == 6:
                display_man(wrong_guesses)
                print(f"Sorry, you've lost! The word was: {answer}")
                running = False  # End the game since the player has lost
        
        sleep(1)  # Pause for a moment to improve user experience

if __name__ == "__main__":
    main()

