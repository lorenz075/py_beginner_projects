from os import system, name
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def append_card(cards, list):
    card = random.choice(cards)
    appended_card = list.append(card)
    CARDS.remove(card)
    return appended_card


def sum_list(list):
    sum = 0
    for card in list:
        sum += card
    return sum


def check_for_11(array, sum_array):
    exist_count = array.count(11)
    sum = sum_list(array)
    if exist_count > 0 and sum > 21:
        sum_array -= 10
    return sum_array


def prints():
    print(f"     Your cards: {PLAYER_CARDS}, current score: {sum_player}")
    print(f"     Computer's first card: {PC_CARDS[0]}")


while True:
    play_again = input("Do you want to play?(Y/n) ")
    if play_again == 'y':
        CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8,
                 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        PC_CARDS = []
        PLAYER_CARDS = []
        clear()
        # get initial cards
        for i in range(2):
            append_card(CARDS, PC_CARDS)
            append_card(CARDS, PLAYER_CARDS)

        sum_player = sum_list(PLAYER_CARDS)
        sum_pc = sum_list(PC_CARDS)
        # Begin the game

        prints()

        # Inicial win situation
        if sum_player == 21:
            print("You Have a blackjack, you win!!")
            print("You win")
        # logica
        elif sum_player < 21:
            while True:
                another_card = input(
                    "Type 'y' to get another card, type 'n' to pass:")
                # Yes logic
                if another_card == 'y':
                    append_card(CARDS, PLAYER_CARDS)
                    sum_player = sum_list(PLAYER_CARDS)
                    if sum_player < 21:
                        prints()
                        continue
                    elif sum_player == 21:
                        prints()
                        print("You Have a blackjack, you win!!")

                        break
                    else:
                        prints()
                        print(
                            f"     PC cards: {PC_CARDS}, final score: {sum_pc}")
                        print("You went over. You lose!!")

                        break
                # No logic
                elif another_card == 'n':
                    sum_pc = sum_list(PC_CARDS)
                    while sum_pc <= sum_player:
                        new_card = append_card(CARDS, PC_CARDS)
                        sum_pc = sum_list(PC_CARDS)
                        eleven = check_for_11(PC_CARDS, sum_pc)
                        sum_pc = eleven
                    if sum_pc == 21:
                        print(
                            f"     PC cards: {PC_CARDS}, final score: {sum_pc}")
                        print("     You lose, PC has a blackjack!")

                        break
                    elif sum_pc < 21:
                        prints()
                        print(
                            f"     PC cards: {PC_CARDS}, final score: {sum_pc}")
                        print("PC beats you!")

                        break
                    else:
                        print(
                            f"        PC cards: {PC_CARDS}, final score: {sum_pc}")
                        print("You win")

                        break
    else:
        break
