from os import system, name
import random
from data_logo import data, logo, vs


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the guess and returns if it is right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# Display art
print(logo)
score = 0
account_b = random.choice(data)
# Make the repeatable
while True:

    # Generate a random account
    account_a = account_b
    account_b = random.choice(data)
    if account_b == account_a:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # Get follower count of each count
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Use if statement to check if user is correct

    # Give user feedback on their guess
    if is_correct:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
    else:
        print(f"WROOOOOONG. Final score: {score}")
        break


# Making the account at p B become the next at p A
