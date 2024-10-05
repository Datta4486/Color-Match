import random
from colorama import Fore, Style

Repeat = 1
ColorList = ["🟦","🟥","🟩","🟨","🟧","🟫","⬛","🟪","⬜"]


print("Welcome to " + Fore.CYAN + "Color Match" + Style.RESET_ALL + "!")
print("Do you want to know the basics of this simple game?")


while True:
    RulesInput = str(input("").lower)
    if RulesInput in ["yes","no","y","n"]:
        if RulesInput == "yes":
            print("The game sets a order of color emojis in a randomized order and you must guess the order by switching 2 colors.\nFor every switch, you get a message notifying you about the no of colors which match the randomized order.\nMatch all of the colors in as few tries as possible. ")
            break
        else:
            break
    else:
        print("Invalid Input. Type either yes or no.") 

print("Do you want to play a game?")


while True:
    PlayGame = str(input("").lower)
    if PlayGame in ["y","n","yes","no"]:
        break
    else:
        print("Invalid Input. Type either yes or no.")

if PlayGame == "yes":
    while Repeat == 1:

        print("Choose the no of colors you want to match. Max no of colors is 9")
        
        while True:
            try:
                ColorNo = int(input(""))
                if ColorNo in [1,2,3,4,5,6,7,8,9]:
                    break
                else:
                    print("No should be between 1 - 9")
            except ValueError:
                print("Make sure that the input is a number and not a string")

        CPUList = []
        CPUList = random.sample(ColorList,ColorNo)

            








