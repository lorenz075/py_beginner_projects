import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]

while True:
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if user_choice <= 3 and user_choice > 0 :
            print(game_images[user_choice])
            computer_choice = random.randint(0, 2)
            print("Computer chose:")
            print(game_images[computer_choice])
            
            if user_choice == 0 and computer_choice == 2:
                print("You win!")
            elif computer_choice == 0 and user_choice == 2:
                print("You lose")
            elif computer_choice > user_choice:
                print("You lose")
            elif user_choice > computer_choice:
                print("You win!")
            elif computer_choice == user_choice:
                print("It's a draw")
            else:
                break    
                
            end_game = input("type y to continue and anything else to quit: ")
            if end_game == "y":
                pass
            else :
                print("Closing game")
                break
    except:
        print("Invalid output")        
