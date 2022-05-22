machine = {"water" : 400,
           "milk" : 540,
           "coffee" : 120,
           "cups" : 9,
           "money" : 550}

signal = True

menu = ("espresso", "latte", "cappuccino")

def add_ingredients(product, x, y, z, w):
    for value, ingredient in zip((x, y, z, 1, w), ("water", "milk", "coffee", "cups", "money")):
        products[product][ingredient] = value
    
products = {key: {} for key in menu}

add_ingredients("espresso", 250, 0, 16, -4)
add_ingredients("latte", 350, 75, 20, -7)
add_ingredients("cappuccino", 200, 100, 12, -6)

def remaining():
    texts = ("ml of water", "ml of milk", "g of coffee beans", "disposable cups", "of money")
    for text, value in zip(texts, machine):
        print(machine.get(value), text)
        
def buy():
    global machine
    
    def operation(n):
        for ingredient in machine:
            machine[ingredient] -= products[menu[n-1]].get(ingredient)
    
    def validate(n):
        for ingredient in machine:
            if machine[ingredient] < products[menu[n-1]].get(ingredient):
                print(f"Sorry, not enough {ingredient}!")
                return None
        print("I have enough resources, making you a coffee!")
        operation(n)
        
    
        
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    
    n = input()
    
    if n.isdigit():
        validate(int(n))
    else:
        pass
    
def fill():
    def text(x):
        print(f"Write how many {x} you want to add:")
        
    text("ml of water")
    machine["water"] += int(input())

    text("ml of milk")
    machine["milk"] += int(input())

    text("grams of coffee")
    machine["coffee"] += int(input())
    
    text("how many disposable cups")
    machine["cups"] += int(input())
    
def take():
    print("I gave you $" + str(machine["money"]))
    machine["money"] = 0

def options(x):
    global signal
    
    if x == "buy":
         buy()
    elif x == "fill":
        fill()
    elif x == "take":
        take()   
    elif x == "remaining":
        remaining()
    elif x == "exit":
        signal = False
"""def max_min():
    max_coffees = min(water//200, milk//50, coffee//15)
    print("Write how many cups of coffee you will need:")
    cups = int(input())

    if cups > max_coffees:
        print(f"No, I can make only {max_coffees} cups of coffee")
    elif cups == max_coffees:
        print("Yes, I can make that amount of coffee")
    else:
        print(f"Yes, I can make that amount of coffee (and even {max_coffees - cups} more than that)")"""

def need():
    print(f"For {cups} cups of coffee you will need:")
    print(f"{cups * 200} ml of water")
    print(f"{cups * 50} ml of milk")
    print(f"{cups * 15} g of coffee beans")
    
def main():
    while signal:
        print("Write action (buy, fill, take, remaining, exit):")
        options(input())

if __name__ == "__main__":
    main()