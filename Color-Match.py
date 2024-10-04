import random
from colorama import Fore, Style



print("Welcome to " + Fore.CYAN + "Color Match" + Style.RESET_ALL + "!")
print("Do you want to know the basics of this simple game?")
RulesInput = str(input("").lower)

while True:
    if RulesInput in ["yes","no"]:
        if RulesInput == "yes":
            print("The game sets a order of color emojis in a randomized order and you must guess the order by switching 2 colors.\nFor every switch, you get a message notifying you about the no of colors which match the randomized order.\nMatch all of the colors in as few tries as possible. ")
        else:
            break
    else:
        print("Invalid Input. Type either yes or no.") 

print("Do you want to play a game?")   
