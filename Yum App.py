"""
Munch - An app that produces a menu from your favorite dishes,
and gives you a list of ingredients if required.

"""
# ------ Imports ------

from random import choice

# ------ A. Functions------

# A1. Choose Dishes

def chooseDishes(days):            # --- FunctionHead ---
    while len(myMenu) < int(days): # stop condition - when the length of myMenu is no longer < the requested number of days (i.e now false)
        chosenDish = choice(favoriteDishes) # (our favoriteDishes contain strings, so our chosenDish would likely contain strings as well)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu...")

    print()
    #print(myMenu)

    for dish in myMenu:
        print(dish)

    print()

    print("Out of all these dishes, my favorite has to be... " + choice(myMenu))

    print()
    '''
    1. Choose a random dish from favoriteDishes list - Done!
    2. Check dish hasn't already been chosen, if not add to myMenu - Done!
    3. Repeat until we have required number of dishes our user asked for in myMenu - Done!

    '''
def buildShoppingList():
    
    if "Pizza" in myMenu:
        shoppingList.append(pizza)
    if "Burgers" in myMenu:
        shoppingList.append(burgers)
    if "Pommes" in myMenu:
        shoppingList.append(pommes)
    if "Chicken Sauce" in myMenu:
        shoppingList.append(chickenSauce)
    if "Fish Soup" in myMenu:
        shoppingList.append(fishSoup)
    if "Spaghetti" in myMenu:
        shoppingList.append(spaghetti)
    if "Veggies" in myMenu:
        shoppingList.append(veggies)
    
    #print(shoppingList)
        
    for element in shoppingList:
        for dish in element:
            print(dish)
    print()
    print("There you go! Enjoy your meal and have a great week!")


def endProgram():

    print()
    print("I'll take that as a 'No'. Enjoy your meal and have a great week! :)")

    
# A2. Build shopping lists


# ------ B. Lists (in no particular order) ------
myMenu = []

shoppingList = []

favoriteDishes = []

favoriteDishes.extend(["Pizza", "Burgers", "Pommes", "Chicken Sauce", "Fish Soup", "Spaghetti", "Veggies"])

pizza = ["Pizza Base", "Tomatoes", "Mozarella", "Chillis", "Onions"]

burgers = ["Burger Base", "Beef", "Lettuce", "BBQ Sauce", "Onions"]

pommes = ["Baby Potatoes", "Salt", "Cooking oil"]

chickenSauce = ["Chicken", "Onions", "Pepper", "Chicken Spices"]

fishSoup = ["Fish", "Scent Leaves", "Onions", "Fish Spices"]

spaghetti = ["Spaghetti", "Beef", "Onions", "Tomatoes"]

veggies = ["Cabbage", "Cucumber", "Spinach"]



# 1. How many days to plan for?

print("Hello, I'm Yum! I'll help you to plan your dinner menu...")

answer = input("How many days would you like me to plan for? ")

print("Ok, I'm going to plan",answer,"dinner(s) from your favorite meals list.")

      
# 2. call Function to Choose dishes (create a list to choose dishes from and a function to choose the dishes and auto-populate the myMenu list)

chooseDishes(answer)

#print(favoriteDishes)

# 3. Build a shopping list

answer = input("Would you like a shopping list for these dishes? Enter 'Y' for 'Yes' or 'N' for 'No'. ")
print()

if answer.lower() == "y":
    # call buildShoppingList
    buildShoppingList()

else:
    endProgram()
