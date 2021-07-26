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

bids = {
    
}


while True:
    name = input("Type your name: ")
    bid_value = input("Your bid: ")
    bids[name] = bid_value
    key_list = list(bids.keys())
    val_list = list(bids.values())
    
    question = input("Do you want to add more biders? type 'yes' or 'no' ")
    if question == "yes":
        clear()
        continue
    if question == "no":
        #get the highest bid using max()
        all_values = bids.values()
        max_value = max(all_values)
        position = val_list.index(max_value)
        winner = key_list[position]
        print(f"The winner is {winner} with a bid of {max_value}")
        break
    
