from main import MENU, resources


# 3.Print report
def printReport():
    """Print Report Resources"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    return print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney:$0")


def coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many quarters?: ")) * 0.1
    total += int(input("how many quarters?: ")) * 0.05
    total += int(input("how many quarters?: ")) * 0.01
    return total


source_coffee = True
while source_coffee:
    # 1.Prompt user by asking "What would you like? (espresso/latter/cappuccino):"
    source = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # 2.Turn off the Coffee Machine by entering "off" to the prompt
    if source == 'off':
        source_coffee = False
    elif source == 'report':
        printReport()
    elif source == 'espresso' or source == 'latte' or 'cappuccino':
        coins()



