"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip Hájek
email: filipp.hajek@gmail.com
discord: Filip filip936
"""
import random
import time

print("Hi there!")
print("-" * 70)
#number_r = str(random.randint(1000,9999))  
number_r = "2016"
print("I've generated a random 4 digit number for you.", "Let's play a bulls and cows game.") 
print("-" * 70)
guess_number = 0
round_count = 0
time_start = time.time()

# smyčka pro hádání
while guess_number != number_r:
    guess_number = (input("Enter a number:"))
    round_count = round_count + 1
    if not guess_number.isnumeric():
        print("You have not entered a number!")
        continue
    elif len(guess_number) != 4:
        print("You have not entered a 4 digit number!")
        continue
    elif guess_number == number_r:
        time_end = time.time()
        total_time = time_end - time_start
        print("Congratulations, you won in ", round_count, "rounds.")
        print("It took you", round(total_time, 2), "seconds to guess the number.")
        print("-" * 70)
        break
    else: 
        bulls = 0
        if bulls == 1:
            text_b = "Bull"
        else:
            text_b = "Bulls"
        cows = 0
        if cows == 1:
            text_c = "Cow"
        else:
            text_c = "Cows"

        for i, digit in enumerate(guess_number):
            if digit == number_r[i]:
                bulls += 1
            elif digit in number_r:
                cows += 1
        print("-" * 70)
        print(guess_number)
        print(text_b, bulls, text_c, cows)
        print("-" * 70)

