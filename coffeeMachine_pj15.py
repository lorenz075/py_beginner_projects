MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappucino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "money": 0
}

def show_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']} ")

def calculate_given_money():
    pennies = 0.1
    nickles = 0.05
    dimes = 0.10
    quarters = 0.25
    
    n_of_quarters = float(input("How many quarters?: "))
    n_of_dimes = float(input("How many dimes?: "))
    n_of_nickels = float(input("How many nickels?: "))
    n_of_pennies = float(input("How many pennies?: "))
    
    given_money = (quarters*n_of_quarters) + (dimes*n_of_dimes) + (nickles*n_of_nickels) + (pennies + n_of_pennies)
    return given_money

def check_enough_money(drink, given_money):
    cost = MENU[drink]['cost']
    if cost < given_money:
        resources['money'] += cost
        change = given_money - cost
        print(f"Here is ${round(change, 2)} in change")
        print(f"Here is your ☕ {drink}")
    elif cost == given_money:
        resources['money'] += given_money
        print(f"Here is your ☕ {drink}")
    else:
        False    

def calculate_rest(drink, ingredient):
    cost =  MENU[drink]["ingredients"][ingredient]
    resource = resources[ingredient]
    if resource >= cost:
        resources[ingredient] = resource - cost
        return resource - cost
    else:
        return False
    
#Ask the client
while True:
    client_choice = input("What would you like? (espresso/latte/cappucino): ").lower()
    if client_choice == 'off':
        break
    while True:
        if client_choice == 'report':
            show_report()
            break
        
        elif client_choice == 'espresso':
            if not calculate_rest(client_choice, 'water'):
                print("Sorry, not enough water.")
                break
            if not calculate_rest(client_choice, 'coffee'):
                print("Sorry, not enough coffee.")
                break
            else:
                print("Insert the coins.")
                value_of_coins = calculate_given_money()
                enough_money = check_enough_money('espresso', value_of_coins)
                break
            
        elif client_choice == 'latte':
            if not calculate_rest(client_choice, 'water'):
                print("Sorry, not enough water.")
                break
            if not calculate_rest(client_choice, 'coffee'):
                print("Sorry, not enough coffee.")
                break
            if not calculate_rest(client_choice, 'milk'):
                print("Sorry, not enough milk.")
                break
            else:
                print("Insert the coins.")
                value_of_coins = calculate_given_money()
                enough_money = check_enough_money('latte', value_of_coins)
                break
            
        elif client_choice == 'cappucino':
            if not calculate_rest(client_choice, 'water'):
                print("Sorry, not enough water.")
                break
            if not calculate_rest(client_choice, 'coffee'):
                print("Sorry, not enough coffee.")
                break
            if not calculate_rest(client_choice, 'milk'):
                print("Sorry, not enough milk.")
                break
            else:
                print("Insert the coins.")
                value_of_coins = calculate_given_money()
                enough_money = check_enough_money('cappucino', value_of_coins)
                break
        
            