def game():
    #imports
    import random
    import time
    
#Defining, initialising and assigning variables
    luckyDraw = []
    chosenNumbers = []
    true = 0
    false = 0
    number = 0

#Loop used to store 5 different numbers into a list with a repeating algorithm for a computer to execute
    for number in range(5):
        lucky = random.randint(1,100)
        luckyDraw.append(lucky)

    print("In this game of lottery, you will choose 5 numbers between 1 and 100, if it all matches the lucky drawn numbers, you will win £1000")
    time.sleep(5)

#A loop designed to check if the numbers inputted are the same as the random numbers as well as inputting the numbers
    for index in range(0, len(luckyDraw)):
        number = int(input("Please choose a number between 1 - 100: "))
        if number > 100:
            print("\n")
            game()
        
        else:
            chosenNumbers.append(number)
            if number == luckyDraw[index]:
                true = true + 1
                index = index + 1
            
            else:
                false = false + 1

    print("Now that you have inputted 5 chosen numbers, lets see today's lucky draw.")
    print("\n")
    time.sleep(3)
    print("Processing")
    time.sleep(1)
    print("Processing")
    time.sleep(1)
    print("Processing")
    time.sleep(1)
    print("\n")

    print(luckyDraw)

#Final verdict based on the inputted numbers (user devised function)
    if false == 0:
        print("Congrats, you have won £1000")
    else:
        print("I'm sorry, you do not win any money")
    
    choice = input("Want to play again: ")
    if choice in ["Y", "y", "yes", "Yes"]:
        print("Starting new game")
        time.sleep(5)
        print("\n")
        game()
    
    else:
        print("Thank you, Goodbye")
        quit()
game()