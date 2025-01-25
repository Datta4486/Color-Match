import random
from colorama import Fore, Style

#To repeat code again
Repeat = 1

#For showing the Emojis
ColorList = ["🟦","🟥","🟩","🟨","🟧","🟫","⬛","🟪","⬜"]

#For the user choosing which color to choose based on names
ColorDict = {"Blue":"🟦","Red":"🟥","Green":"🟩","Yellow":"🟨","Orange":"🟧","Brown":"🟫","Black":"⬛","Purple":"🟪","White":"⬜"}

#For ColoredText depending on no of tries
def TextColorFunctionForTries(x):
    if x == 1:
        return Fore.CYAN
    elif x < 10:
        return Fore.GREEN
    elif x < 20: 
        return Fore.LIGHTRED_EX
    else:
        return Fore.BLACK

print("Welcome to " + Fore.CYAN + "Color Match" + Style.RESET_ALL + "!")
print("Do you want to know the basics of this simple game?")

#To get key from value
def KeyValueReturn(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None  # If the value isn't found


#Rules
while True:
    RulesInput = str(input("").lower())
    if RulesInput in ["yes","no","y","n"]:
        if RulesInput == "yes":
            print("You get a set of random colors and you should guess the correct position of each color by switching positions of 2 colors.\nFor every switch, you will be notified about the number of colors matched.\nMatch all of the colors in as few tries as possible. ")
            break
        else:
            break
    else:
        print("Invalid Input. Type either 'yes'or 'no'.") 


print("Do you want to play a game?")


while True:
    PlayGame = str(input("").lower())
    if PlayGame in ["y","n","yes","no"]:
        break
    else:
        print("Invalid Input. Type either 'yes' or 'no'.")

#Actual Game
if PlayGame in ['y','yes']:
    angerColorNo = 0 #To react if specific incorrect actions are done again
    TwoColorsChosen = 0 #For reactions when only 2 colors are chosen
    while True:

        print("Choose the number of colors that you want to match. Maximum number of colors is 9.")
        
        #Typo check
        while True:
            try:
                ColorNo = int(input(""))
                #Funny Ranting about miniscule things
                if ColorNo == 1:
                    if angerColorNo == 0:
                        angerColorNo+= 1
                        print("You can't play this game with just 1 color. \nChoose a number that isn't 1")
                    elif angerColorNo == 1:
                        angerColorNo += 1
                        print("I am not sure if you didn't see the last sentence but you can't play with 1 color. \nChoose any other number. ")
                    elif angerColorNo == 2:
                        angerColorNo += 1
                        print("Really want to be the 'Free Thinker' who oppose instructions, huh? Now, do as I say.")
                    elif angerColorNo == 3:
                        angerColorNo += 1
                        print("Fine. If you do not listen, I will not too.")
                    else:
                        print("...")
                        
                #Just for checking valid option
                elif ColorNo in [2,3,4,5,6,7,8,9]:
                    if ColorNo == 2:
                        TwoColorsChosen +=1
                    if angerColorNo >2:
                        print("Finally!")
                    break

                else:
                    print("Number should be between '2 - 9'")
            except ValueError:
                print("Make sure that the input is a number and not a string")

        #Randomized Computer List
        CPUList = []
        CPUList = random.sample(ColorList,ColorNo)

        #Randomized UserList
        UserList = []
        UserList = random.sample(CPUList,ColorNo)

        #To avoid the possibility of UserList and CPUList being equal by sheer luck
        while True:
            if CPUList != UserList:
                break
            else:
                UserList  = random.sample(CPUList,ColorNo)


        tries = 0
        while True:
            #End the game if they match
            if UserList == CPUList:
                break

            while True:

                #To show the names of colors below
                ColorNameList = []

                for M in UserList:
                    ColorNameList.append(KeyValueReturn(ColorDict,M))


                #Same function but with lowercase strings for easy relation checking with Initial And Final C which has lower function.
                ColorNameListLower = []
                for i in ColorNameList:
                    ColorNameListLower.append(i.lower())
                    

                print("\n")
                print(UserList)
                print(ColorNameList)
                print(CPUList)

                CorrectPlaceNo = 0 #No of correctly matched colors reset
                            
                for i in CPUList:
                    CPUPos = CPUList.index(i)
                    if UserList[CPUPos] == CPUList[CPUPos]:
                        CorrectPlaceNo += 1
                
                print("There are " + str(CorrectPlaceNo) + " matched colors")
                print("Specify the color that you want to change its position : ")


                #Switching colors logic
                while True:
                    InitialC = str(input("").lower())
                        
                    if InitialC in ColorNameListLower:
                        break
                    else:
                        print("The color you specified does not exist. Try again.")

                print("Specify the color that you want to exchange the position with the previous chosen color : ")

                while True:
                    FinalC = str(input("").lower())
                    if FinalC in ColorNameListLower and FinalC != InitialC:
                        break
                    elif FinalC == InitialC:
                        print("You chose the same color, choose a different one.")
                    else:
                        print("The color you specified does not exist. Try again")

                print("Are you sure you want to switch " + InitialC + " with " + FinalC + "?")

                while True:
                    SwitchAnswer = str(input("").lower())
                    if SwitchAnswer in ["yes","no","y","n"]:
                        break
                    else:
                        print("Wrong Input. Type either 'yes'or 'no'.")
                
                if SwitchAnswer in ["yes","y"]:
                    tries += 1
                    UserList[ColorNameListLower.index(InitialC)],UserList[ColorNameListLower.index(FinalC)] = UserList[ColorNameListLower.index(FinalC)],UserList[ColorNameListLower.index(InitialC)]
                    break


        #Congratulations message and ranting as usual               
        if ColorNo == 2 and TwoColorsChosen == 1:
            print("Yay, you just beat this game on the easiest mode. \nWhat made you choose just 2 colors to match? \nAnyhow, would you like to play another game?  \nHopefully, in the next game I would like to have \033[1m YOU \033[0m not choose the 'Daddy! Can I play this?' difficulty.")
        elif ColorNo == 2 and TwoColorsChosen == 2:
            print("I thought I told someone to choose anything expect 2 colors. Do you just want to hear (or in this case - see) what I would say, huh? \nAnyhow, would you like to play another game (hopefully it isn't 2 colors again)?")
        elif ColorNo == 2 and TwoColorsChosen == 3:
            print("You are probably just choosing two colors just to hear me rant, huh? I will not feed this behaviour anymore. \nWould you like to play another game?")
        elif ColorNo == 2 and TwoColorsChosen > 3:
            print("... \nWould you like to play a game?")
        elif tries == 1 and ColorNo != 2:
            print("WOW! You have succesfully beat this game in only a try. \nI am not sure if it's just sheer luck or you just have a good gaming chair. \nAnyhow, would you like to play again?")
        else:
            print("Congratulations! You matched all of the colors" + TextColorFunctionForTries(tries) ,tries,"tries" + Style.RESET_ALL + ".\nWould you like to play again?")

        while True:
            ReplayAnswer = str(input("").lower())
            if ReplayAnswer in ["yes","y","n","no"]:
                break
            else:
                print("Wrong input. Either type 'yes' or 'no'")
        if ReplayAnswer in ['n','no']:
            break


#Funny
else:
    print('Why even bother running this program?')                
                    








