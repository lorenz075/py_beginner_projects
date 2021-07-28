import random

NUMBERS_ARRAY = []

def fill_numbers_array():
    for i in range(100):
        NUMBERS_ARRAY.append(i+1)

fill_numbers_array()

def guessing(n_of_attempts, right_choice):
        attempts = n_of_attempts
        while attempts > 0:
            print(f"You have {attempts} remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == right_choice:
                print("You got it!")
                break
            elif guess > right_choice:
                print("Too high.")
                attempts -= 1
            elif guess < right_choice:
                print("Too low.") 
                attempts -= 1   
        if attempts == 0:
            print(f"No more guessing for you! The right number was {right_choice}")   

def main_game(difficulty):
    right_choice = random.choice(NUMBERS_ARRAY)
    if difficulty == 'easy':
        guessing(10, right_choice) 
    elif difficulty == 'hard':
        guessing(5, right_choice)

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")
    main_game(difficulty)
    
while True:       
    start_game()            
    continue_game = input("Wanna play again?(y/n)")
    if continue_game == 'y':
        continue
    else:
        break

