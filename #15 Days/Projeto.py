from main import MENU, resources


def is_resource_sufficient(order_ingredients):
    # 4. Check resources sufficient?
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True



def coins():
    # 5.Process coins
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_sucessful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

profit = 0
choice_source = True
while choice_source:
    
    # 1.Prompt user by asking "What would you like? (espresso/latter/cappuccino):"
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    # 2.Turn off the Coffee Machine by entering "off" to the prompt
    if choice == 'off':
        choice_source = False

    # 3.Print report
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coins()
            if is_transaction_sucessful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])




