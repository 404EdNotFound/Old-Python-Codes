def game():
    import time

    print("For this game between 2 players, the first person to reach sqaure 100 or more wins the game. There are obstacles such as ladders and snakes which can give you an opportunitiy or a punishment.")

def playgame():
    import random
    import time

    name1 = ""
    name2 = ""
    player1 = ""
    player2 = ""

    name1 = input("Please enter your name: ")
    name2 = input("Please enter your name: ")

    player1 = name1
    player2 = name2

    turn = ""
    square1 = 0
    square2 = 0
    roll = 0
    snake = 0
    ladder = 0

    SNAKES = [17, 54, 62, 64, 87, 93, 95, 99]
    SNAKES2 = [7, 34, 19, 60, 24, 73, 75, 78]

    LADDERS = [4, 9, 20, 28, 40, 51, 63, 71]
    LADDERS2 = [14, 31, 38, 84, 59, 67, 81, 91]

    while square1 <= 100 and square2 <= 100:
        turn = player1
        print(turn, "press enter to roll the dice.")
        input()
        roll = random.randint(1,6)
        square1 += roll

        print("You rolled a: ", roll, "Go to square: ", square1)

        while square1 < ladder:
            if square1 in LADDERS:
                ladder = random.choice(LADDERS2)
                if square1 < ladder:
                    square1 = ladder
                    print("Hooray, you landed on a ladder, go to square", square1)
                    break
            
                else:
                    random.choice(LADDERS2)
            
            else:
                break
        
        while square1 > snake:
            if square1 in SNAKES:
                snake = random.choice(SNAKES2)
                if square1 > snake:
                    square1 = snake
                    print("Oh no, you landed on a snake, go to square: ", square1)
                    break

                else:
                    random.choice(SNAKES2)
            
            else:
                break
        
        turn = player2
        print(turn, "press enter to roll the dice.")
        input()
        roll = random.randint(1,6)
        square2 += roll

        print("You rolled a: ", roll, "Go to square: ", square2)

        while square2 > ladder:
            if square2 in LADDERS:
                ladder = random.choice(LADDERS2)
                if square2 < ladder:
                    square2 = ladder
                    print("Hooray, you landed on a ladder, go to square", square2)
                    break
            
                else:
                    random.choice(LADDERS2)
            else:
                break
        
        while square2 > snake:
            if square2 in SNAKES:
                snake = random.choice(SNAKES2)
                if square2 > snake:
                    square2 = snake
                    print("Oh no, you landed on a snake, go to square: ", square2)
                    break

                else:
                    random.choice(SNAKES2)
            else:
                break
        
        if square1 >= 100:
            print(player1, "wins")
        
        elif square2 >= 100:
            print(player2, "wins")
        
        print("Do you want to start a new game?: ")
        choice = input()
        if choice in ["Yes", "yes", "y", "Y"]:
            print("Since this game hasn't been developed yet, it is set to only play new game.")
            print("Starting new game")
            time.sleep(3)
            print("\n")
            game()
            playgame()
        
        else:
            print("Thank you, goodbye")
            quit()
game()
playgame()