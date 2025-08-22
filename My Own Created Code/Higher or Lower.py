#Procedure / Subprogram defined
def game():
    import random #Imports are made for random and time
    import time

#Variables defined, assigned and initialised
    chosenNumbers = []
    choice = ""
    point = 0

#A loop is used to store random added numbers into a list
    for index in range (1,21):
        chosen = random.randint(1,101)
        chosenNumbers.append(chosen)

    print("For this game, a random number will pop out, you have to try and guess if the next number is higher or lower than the previous one. The game will keep on going until you guess wrong.")
    time.sleep(5)

#Range of loops, if and else statements used to check if the number is higher or lower, plus a mixture of relational and logical operatiors
    for index in range(0, len(chosenNumbers)):
        print(chosenNumbers[index], "is the chosen number, is the next number higher or lower: ")
        choice = input()
        if choice == "Higher" or choice == "higher" and chosenNumbers[index] < chosenNumbers[index+1]:
            print("That was the right guess")
            point = point + 1
            index = index + 1
        
        elif choice == "Lower" or choice == "lower" and chosenNumbers[index] > chosenNumbers[index+1]:
            print("That was the right guess")
            point = point + 1
            index = index + 1
        
        else:
            print("That was a wrong guess")
            print("You scored: ", point)
            print(chosenNumbers)
            print("Here was the list of numbers")
            break
        
    print("\n")
    secondChoice = input("Do you want to play again: ")
    if secondChoice in ["Yes", "yes", "y", "Y"]:
        print("A new game will be starting soon...")
        time.sleep(5)
        print("\n")
        game()
    else:
        print("Thank you, goodbye.")
game()