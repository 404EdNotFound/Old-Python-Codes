def game():
    print("Microsoft © 1983 - 2022")
    print("This game is a choose your own adventure style where you get to choose your own decisions which can impact you on the game.")
    name = input("Please enter your name: ")
    print("Would you like to start a new game: ")
    choice = input()

    if choice in ("Yes", "yes", "Y", "y"):
        print("Starting game...")
        print("\n")
    
    else:
        print("Goodbye")
        quit()
    
    def playgame():
        items = ["Sword", "Bucket", "Hammer", "Pickaxe"]
        bag = []
        print(name, "you are stuck inside of a room with the door locked, inside the room consists of useful items: sword, bucket, hammer, pickaxe. You are required to take all of them.")
        print("Do you wish to take all of the items?")
        choice = input()

        if choice in ("Yes", "yes", "y", "Y"):
            print("Good Choice")

            for item in items:
                bag.append(item)
            
            print("The items are now in your bag. You are able to transfer to a different room.")
        
        else:
            print("Unfortunately, you end up trapped in the room untli you breathe your last. Goodbye forever.")
            print("Would you like to play again?")
            choice2 = input()

            if choice2 in ("Yes", "yes", "y", "Y"):
                print("Starting new game.")
                print("\n")
                playgame()
            
            else:
                print("Thank you, goodbye")
                quit()
        
        print("\n")

        print("You now enter a room where its pouring down with lave from above. You need to quickly think of a quickfire solution before you end up getting scattered by the lava. Which items wlil you use in your bag?")
        objects = input()

        if objects == "Pickaxe" or objects == "pickaxe":
            print("The pickaxe is useful as you mine a block from the room to stop the lava from pouring further. Would you like to keep the pickaxe.")
            pickaxe_choice = input()

            if pickaxe_choice in ("Yes", "yes", "Y", "y"):
                print("The Pickaxe is still in the bag.")
            
            else:
                bag.pop("Pickaxe")
                print("The Pickaxe is no longer in your bag")
            print("The items you currently have: ", bag)

        elif objects == "Bucket" or objects == "bucket":
            print("The bucket is useful for collecting lava for later use. However, it doesn't stop you from getting past the room as lava is still there. The Lava eventually burns the entire plcae and take you with it. Farewell.")
            print("Would you like to play again?")
            choice2 = input()

            if choice2 in ("Yes", "yes", "y", "Y"):
                print("Starting new game.")
                print("\n")
                playgame()
            
            else:
                print("Thank you, goodbye")
                quit()
        
        elif objects == "Sword" or objects == "sword":
            print("The sword is less protection from the lava. The lava decides to scatter both you and the sword. Farewell.")
            print("Would you like to play again?")
            choice2 = input()

            if choice2 in ("Yes", "yes", "y", "Y"):
                print("Starting new game.")
                print("\n")
                playgame()
            
            else:
                print("Thank you, goodbye")
                quit()
        
        elif objects == "Hammer" or objects == "hammer":
            print("Unfortunately, the hammer is more useful in repairing instead of stopping liquid such as lava. There goes you and the hammer, scattered by the lava")
            print("Would you like to play again?")
            choice2 = input()

            if choice2 in ("Yes", "yes", "y", "Y"):
                print("Starting new game.")
                print("\n")
                playgame()
            
            else:
                print("Thank you, goodbye")
                quit()

        print("\n")
        
        list = ["Fishing Rod", "Net", "Metal Bat", "Axe"]
        print("Now, you have come across a room with multiple items lying on the floor, you are required to take only ONE of these items. Which one will it be: An Axe, A Metal Bat, A Fishing Rod or a Net")
        decision = input()

        for item in list:
            if item == decision:
                bag.append(decision)
                print("The item", decision, "is added to your bag, you might need it for later use.")
                break
            
            else:
                print("Checking...")

                if item not in list:
                    print("You have decided to pass through without collecting any items lying on the floor and stayed with the current items.")
        
        print("\n")

        print("You come across a lake surrounding with fish and you see them as an opportunity of food for you to keep your energy levels high for later. Do you wish to collect the fish?")
        conscience = input()

        if conscience in ["Yes", "yes", "y", "Y"]:
            print("What item will you use to fish with?")
            decision2 = input()

            for item in bag:
                if decision2 == "Bucket" and item == decision2:
                    print("The Bucket is entirely useful for collecting fish and you use your sword to cut the fish into pieces for later.")

                elif decision2 == "Fishing Rod" and item == decision2:
                    print("The Fishing Rod is useful for collecting fish and you use your sword to cut the fish into pieces for later.")
                
                else:
                    print("Unfortunatley, the items such as the hammer, pickaxe aren't useful for collecting fish and thus caused you to waste your time and starve. Do you wish to continue?")
                    choice2 = input()

                    if choice2 in ("Yes", "yes", "y", "Y"):
                        print("You have decided to continue")
            
                    else:
                        print("Starting new game.")
                        print("\n")
                        playgame()
        
        else:
            print("You have decided to look for fresh water to drink to make you stay hydrated and rejuvinated, you also use this as an oportunity to cleanse yourself before you move on to the next stage.")

        print("You now enter into a forest which involves trees, if you travel further, you see a rock and stone mine which is incredibly useful for later. You need to build a form of shelter to keep you well rested as you would need it for later. Which item will you use.")
        decision3 = input()

        for item in bag:
            if item == decision3 and decision3 == "Pickaxe":
                print("The Pickaxe is incredibly useful for mining for stone and rock in the mines and you aquire the items for building a shelter for you to rest")

            elif item == decision3 and decision3 == "Axe":
                print("The Axe is useful for mining trees as the wood is used to build shelter for later use. However, this causes deforestation as the carbon dioxide is released into the atmosphere and contributes to climate change.")
            
            else:
                print("The items such as the hammer, bucket are not useful for building shelter and yet you remain homeless, you decided to rest outside with no shelter.")
        
        print("Now that you have completed this map, there is one final room and task that you have to face before you are free to go.")
        print("\n")
        print("For the final room, you meet a daredevil that plans to haunt you forever. The only way out of this is by defeating him. What item will you choose")
        combact = input()
        for item in bag:
            if combact == "Sword" and item == combact:
                print("You have used the sword to prepare for combact, you and the daredevil start to clash with one another. You keep this up and have now defeated him. You are finally free to go")
                break
            else:
                print("The other items are not useful to defeat the daredevil, you remain useless and this gives the daredevil the opportunity to defeat you. He will now haunt you for life.")
                break
        
        print("Congrats for making it this far. Do you want to play again.")
        choice2 = input()

        if choice2 in ("Yes", "yes", "y", "Y"):
            print("Starting new game.")
            print("\n")
            game()
            playgame()
            
        else:
            print("Thank you, goodbye.")
    playgame()
game()