import sys # Default module, so you should have it, unless it was deleted 
import admin_command as ad #Imports the admin command python code as "ad"
try:
    room = ""
    house = [["entrance_room", "The entrance room is damp, smells of wet wood, with a singular candle hung in the far corner.", True, False], # Defining the rooms, the description, whether it is lit, and whether it is locked 
            ["living_room", "In the living room, there is a fossilised sofa, and intricate designs have been created by cobwebs.", False, True],
            ["kitchen", "In the kitchen, there's ancient pizza on the counter, poisoning the room with its rotten stentch.", False, True],
            "parlour", "dining hall", "cellar"] 
    puzzles = ["""There is a message by the door saying:
    Go where my hatred burned (literally), in my living room (the door to the north), if you dare, attached is the key
    To recieve light in the living room, solve answer this question:
    In which continent were the Napoleonic Wars fought in?
    A - Europe
    B - Asia
    C - North America""",
    """To recieve light in the kitchen answer this question:
Which country did Admiral Nelson fight for?
    A(Default) - The United States of America
    B - The (at that time known as) United Kingdom of Great Britain and Ireland
    C - The (at that time known as) First French Empire"""]
    items = [["Key of Loathing", "living_room", False]]
    def intro(): # The games introduction function
        global name
        print("Welcome to the Temple of Doom.")
        name = input("Please enter your Horror Games People ID username")
        if name == "omegabetaalphagammaraY": # Secret admin code, in case you need to skip levels
            ad.admin()
        else:
            pass
        print("This game is presented by the Horror Games People Industries!")
        print("© Copyright Horror Games People Industries")
        print("Starting game...")
        print("Hello", name, "immerse yourself in the Temple of Doom, i.e. a temple found buried under London, that the British Government wants you to explore.")
        option = input("""Please choose what to do:
    0(Default) - Yes! Let's go, I like exploring!
    1 - I'm too scared, hire someone else, I am not opening that door""")
        if option == "1":
            print("""GAME OVER!
                    I mean, you can't really play without entering the temple!""")
            sys.exit(1)
        else:
            print("You have opened the rickety door, prepare to be immersed in a new world!")
            level_0()

    def level_0():
        global house, puzzles, items, room # Allowing the function to access the global variables
        room = "entrance_room"
        print(house[0][1])
        print(puzzles[0])
        house[1][3] = False
        while 0==0:
            option = input("""Chosee what to do:
    0(Default) - Enter the living room without light
    1 - Select Option A
    2 - Select Option B
    3 - Select Option C""")
            if option == "2" or option == "3":
                print("""A new message has appeared:
    Nope! You are wrong try again!""")
            elif option == "1":
                print("""A message has appeared:
    You are correct! Progress if you dare!""")
                house[1][2] = True
                break
            else:
                print("Onwards we go into complete darkness!")
                break
        level_1()

    def level_1():
        global house, puzzles, items, room # Allowing the function to access the global variables
        room = "living_room"
        if house[1][2] == False:
            option = input("""Aargh! There's no light, it's too dark!!! What should you do?:
    0(default) - Return to the entrance room
    1 - Wait in the darkness for something to come and kill us""")
            if option == "1":
                print("GAME OVER! I could have told you how you died, but it TOO DARK!!!")
                sys.exit(1)
            else:
                print("Phew, let's go back to the entrance room and start from there!")
                level_0()
        else:
            print(house[1][1]) # Description for the living room
            while 0==0:
                option = input("""AARGH! The room key disintegrated after opening the door, it must have been very old. 
Anyways the message is in a place where his hatred burned.
Therfore, I have located three possible locations in the living room:
    0(Default) - Sofa
    1 - Fireplace
    2 - Fossilised large cobweb structure?""")
                if option == "1":
                    print("Yes, you've found it!")
                    break
                else:
                    print("Nope, not here, please try again!")
            print("""The message says:'In this room, I have hidden the Key of Loathing, you need this to open the next door.
It is in a place where education is gained.'""")
            while 0==0:
                option = input("""I have narrowed down the location of the Key of Loathing to three places
Please choose the one you think it is:
    0(Default) -  Next to the window 
    1 - In the hole in the wall
    2 - In the bookcase""")
                if option == "2":
                    print("Yes, you've found it!")
                    break
                else:
                    print("Nope, not here, please try again!")
            print("Alright it was wrapped in a message which says:")
            print(puzzles[1])
            while 0==0:
                option = input("""Chosee what to do:
    0(Default) - Enter the kitchen without light
    1 - Select Option A
    2 - Select Option B
    3 - Select Option C""")
                if option == "1":
                    print("Well done, we got it right, let's go through to the kitchen.")
                    house[2][2] = True
                    break
                elif option == "2" or option == "3":
                    print("Nope, that's wrong, we better try again.")
                else:
                    print("Alright into the darkness we go.")
            level_2()

    def level_2():
        global house, puzzles, items, room, name # Allowing the function to access the global variables
        room = "kitchen"
        if house[2][2] == False:
            option = input("""Aargh! There's no light, it's too dark!!! What should you do?:
    0(default) - Return to the living room.
    1 - Wait in the darkness for something to come and kill us""")
            if option == "1":
                print("GAME OVER! I could have told you how you died, but it TOO DARK!!!")
                sys.exit(1)
            else:
                print("Phew, let's go back to the living room and start from there again, because I lost the key!")
                level_1()
        else:
            print(house[2][1])
            print("Carrying items UNLOCKED.")
            print(name, """you have now unlocked the ability to carry items. 
Whenever you have to enter something, entering 'item' will allow you to review the items you are carrying, and whether you want to drop them.""")
            

except:
    print("I apolgize, but there has been an error in the game...")
    print("Please report this error to Horror Games People Industries.")
    print("Take a screenshot and tag us on X!")
    print("I am afraid its GAME OVER! Please hold on while we resolve the problem...")
    sys.exit(1)
