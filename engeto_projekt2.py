"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip Hájek
email: filipp.hajek@gmail.com
discord: Filip filip936
"""
import random
import time

def generate_number():
    '''
    Generates a random 4-digit number with unique digits.
    
    Returns:
        str: A string representing a 4-digit number.
    '''
    return str(random.randint(1000, 9999))

def get_guess():
    '''
    Promts the user to enter a guess number.
    
    Returns:
        str: The user's guess number.
    '''
    return input("Enter a number: ")

def validate_guess(guess):
    """
    Validates the user's guess.
    
    Args:
        guess (str): The user's guess.
        
    Returns:
        bool: True if the guess is valid, False if not.
    """
    if not guess.isnumeric():
        print("You have not entered a number!")
        return False
    if len(guess) != 4:
        print("You have not entered a 4 digit number!")
        return False
    if guess[0] == '0':
        print("The number cannot start with 0!")
        return False
    if len(set(guess)) != 4:
        print("The number cannot contain duplicate digits!")
        return False
    return True

def calculate_bulls_and_cows(guess, secret_number):
    """
    Calculates the number of bulls and cows for a given guess.
    
    Args:
        guess (str): The user's guess.
        secret_number (str): The secret number to be guessed.
        
    Returns:
        tuple: A tuple containing the number of bulls and cows.
    """
    bulls = sum(1 for i in range(len(guess)) if guess[i] == secret_number[i])
    cows = sum(1 for i in range(len(guess)) if guess[i] in secret_number and guess[i] != secret_number[i])
    return bulls, cows

def print_result(guess, bulls, cows):
    """
    Prints the result of the guess.
    
    Args:
        guess (str): The user's guess.
        bulls (int): The number of bulls.
        cows (int): The number of cows.
    """
    text_bulls = "Bull" if bulls == 1 else "Bulls"
    text_cows = "Cow" if cows == 1 else "Cows"
    print("-" * 70)
    print(f"{guess} -> {bulls} {text_bulls}, {cows} {text_cows}")
    print("-" * 70)

def play_game(secret_number):
    """
    Plays the bulls and cows game.
    
    Args:
        secret_number (str): The secret number to be guessed.
    """
    round_count = 0
    start_time = time.time()
    
    while True:
        guess = get_guess()
        round_count += 1
        
        if not validate_guess(guess):
            continue
        
        if guess == secret_number:
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Congratulations, you won in {round_count} rounds.")
            print(f"It took you {round(total_time, 2)} seconds to guess the number.")
            print("-" * 70)
            break
        
        bulls, cows = calculate_bulls_and_cows(guess, secret_number)
        print_result(guess, bulls, cows)

def validate_secret_number(secret_number): 
    """
    Validates the secret number to ensure it has unique digits.
    
    Args:
        secret_number (str): The secret number.
        
    Returns:
        bool: True if the secret number is valid, False if not.
    """
    if len(set(secret_number)) != 4:
        return False
    return True 

def main_fce():
    """
    The main function that initializes the game.
    """
    print("Hi there!")
    print("-" * 70)
    while True:
        secret_number = generate_number()
        if validate_secret_number(secret_number): 
            break
    
    print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.") 
    print("-" * 70)
    
    play_game(secret_number)

if __name__ == "__main__":
    main_fce()