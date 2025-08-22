import random
import time

print("Welcome to the rock paper scissors game. Here are the Rules:")
time.sleep(2)
print("Rocks beats Scissors by damaging it")
time.sleep(1)
print("Paper beats Rock by covering it")
time.sleep(1)
print("Scissors beats Paper by cutting it")

print("\n")
name = str(input("Please enter your name: "))
print("Hello", name, "good luck")

time.sleep(3)

def game():
    global choices

    print("\n")
    
    print("Welcome to rock, paper scissors")
    print("Please input your choice here:")
    userchoice = input()

    choices = ["Rock", "Paper", "Scissors"]
    comChoice = random.choice(choices)

    if userchoice == comChoice:
        time.sleep(2)
        print("\n")
        print("Both of you Tie")
        print("Computer picked", comChoice)

    elif userchoice == "Rock" and comChoice == "Paper":
        time.sleep(2)
        print("\n")
        print("Computer picked", comChoice)
        print("Computer wins, Paper beats Rock")

    elif userchoice == "Rock" and comChoice == "Scissors":
        time.sleep(2)
        print("\n")
        print("Computer picked", comChoice)
        print(name, "wins, Rock beats Scissors")

    elif userchoice == "Paper" and comChoice == "Scissors":
        time.sleep(2)
        print("\n")
        print("Computer picked", comChoice)
        print("Computer wins, Paper beats Scissors")
    
    elif userchoice == "Paper" and comChoice == "Rock":
        time.sleep(2)
        print("\n")
        print("Computer picked", comChoice)
        print(name, "wins, Paper beats Rock")

    elif userchoice == "Scissors" and comChoice == "Rock":
        time.sleep(2)
        print("\n")
        print("Computer picked", comChoice)
        print("Computer wins, Rock beats Scissors")

    elif userchoice == "Scissors" and comChoice == "Paper":
        time.sleep(2)
        print("\n")
        print("Computer picked", comChoice)
        print(name, "wins, Scissors beats Paper")

    elif userchoice not in ["Rock", "Paper", "Scissors",]:
        print("Invalid Option, try again")
        game()

    print("Do you want to play again, write yes or no")
    decision_input = str(input())
    while decision_input not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]:
        print("Do you want to play again, write yes or no")
        decision_input = str(input())
    if decision_input in ["Yes", "yes", "Y", "y"]:
        print("\n")
        print("New round is starting soon")
        time.sleep(2)
        game()
    elif decision_input in ["No", "no", "N", "n"]:
        print("Ok, goodbye", name)
        quit()
game()