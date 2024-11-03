import random
from colorama import Fore, Style

#To repeat code again
Repeat = 1

#For showing the Emojis
ColorList = ["🟦","🟥","🟩","🟨","🟧","🟫","⬛","🟪","⬜"]

#For the user choosing which color to choose based on names
ColorDict = {"blue":"🟦","red":"🟥","green":"🟩","yellow":"🟨","orange":"🟧","brown":"🟫","black":"⬛","purple":"🟪","white":"⬜"}



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
            print("The game randomizes a set of colored emojis and you must guess the order by switching colors with each other.\nFor every switch, you get a message notifying you of the number of colors matched right.\nMatch all of the colors in as few tries as possible. ")
            break
        else:
            break
    else:
        print("Invalid Input. Type either yes or no.") 


print("Do you want to play a game?")


while True:
    PlayGame = str(input("").lower())
    if PlayGame in ["y","n","yes","no"]:
        break
    else:
        print("Invalid Input. Type either yes or no.")

#Actual Game
if PlayGame == "yes":
    while Repeat == 1:

        print("Choose the number of colors you want to match. Maximum number of colors is 9 ...")
        
        #Typo check
        while True:
            try:
                ColorNo = int(input(""))
                if ColorNo in [1,2,3,4,5,6,7,8,9]:
                    break
                else:
                    print("Number should be between 1 - 9")
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



        while True:
            #End the game if they amtch
            if UserList == CPUList:
                break

            while True:

                #To show the names of colors below
                ColorNameList = []

                for M in UserList:
                    ColorNameList.append(KeyValueReturn(ColorDict,M))
                    

                print("\n")
                print(UserList)
                print(ColorNameList)

                CorrectPlaceNo = 0 #No of correctly matched colors
                            
                for i in CPUList:
                    CPUPos = CPUList.index(i)
                    if UserList[CPUPos] == CPUList[CPUPos]:
                        CorrectPlaceNo += 1
                
                print("There are " + str(CorrectPlaceNo) + " matched colors")
                print("Specify the color that you want to change its position : ")


                #Switching colors logic
                while True:
                    InitialC = str(input(""))
                    if InitialC in ColorNameList:
                        break
                    else:
                        print("The color you specified does not exist. Try again.")

                print("Specify the color that you want to exchange with the previous chosen color : ")

                while True:
                    FinalC = str(input("").lower())
                    if FinalC in ColorNameList and FinalC != InitialC:
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
                        print("Wrong Input. Type either yes or no.")
                
                if SwitchAnswer in ["yes","y"]:
                    UserList[ColorNameList.index(InitialC)],UserList[ColorNameList.index(FinalC)] = UserList[ColorNameList.index(FinalC)],UserList[ColorNameList.index(InitialC)]
                    break

        print("Congratulations! You win the game. \nWould you like to play again?")

        while True:
            ReplayAnswer = str(input(""))
            if ReplayAnswer in ["yes","y","n","no"]:
                Repeat == 0
                break
            else:
                print("Wrong input. Either type yes or no")



#Funny
else:
    print('Why even bother running this program?')                
                    








