#Step 1 
import random

stages = [''' 
 ''','' '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  brazillian clubs edition    1.0v  '''

print(logo)
word_list = ["sao Paulo", "santos", "palmeiras", "corinthians", "flamengo", "fluminense", "vasco", "botafogo", "cruzeiro", "atletico-mg", "america-mg", "internacional", "gremio", "juventude", "ceara", "sport", "fortaleza", "csa", "criciuma", "xv-de-piracicaba", "operario", "cuiaba", "nautico", "ponte-preta", "guarani", "usac", "vila-nova","goias"]
chosen_word = random.choice(word_list)


display = []
for letter in chosen_word:
    display.append('_')

end_of_game = False
stage_number = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    if len(guess) == 1 and guess in chosen_word:
        for idx ,letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = letter       
        print(f"{' '.join(display)}")
    
    elif guess not in chosen_word:
        print(stages[stage_number])
        stage_number -= 1
        if stage_number == 0:
            print("You lose")
            end_of_game=True
    #end conditions
    if "_" in display:
        continue              
    else :
        print("You've won")
        end_of_game = True           
            
        
    

    