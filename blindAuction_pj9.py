from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}

def get_winner(key_list, val_list, all_values):
        max_value = max(all_values)
        position = val_list.index(max_value)
        winner = key_list[position]
        return winner
    
def get_lists(dictionary):
    key_list = list(dictionary.keys())
    val_list = list(dictionary.values())
    all_values = dictionary.values()
    return key_list, val_list, all_values
        

while True:
    name = input("Type your name: ")
    bid_value = input("Your bid: $")
    bids[name] = bid_value
    key_list, val_list, all_values = get_lists(bids)
    
    question = input("Do you want to add more biders? type 'yes' or 'no' ")
    if question == "yes":
        clear()
        continue
    if question == "no":
        #get the highest bid using max()
        winner = get_winner(key_list, val_list, all_values)
        max_value = bids[winner]
        print(f"The winner is {winner} with a bid of {max_value}")
        break
 
