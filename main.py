import sys  # Default module so you should have it
from tkinter import * #Another default module
import time # Dno't worry this is default too

try: #The code is wrapped in a massive try-except statement to account for bugs

    window = "" #placeholder for the window variable


    def admin(): #function for admin mode
        global is_admin #Defing global variables to be used throughout the program
        print("Greeting, admin, you have unlocked admin mode!")
        print("At every puzzle for light in part 1 typing 'admin' will allow you to access admin mode.")
        is_admin = True
        while 0 == 0:
            ad_level = int(input("""Which level do you wish to skip to (the doors and torches will be unlocked for you)?
    WARNING!!! Not entering an integer will result in the game being terminated, due to an error."""))
            if ad_level == 0 or ad_level == 1 or ad_level == 2 or ad_level == 3 or ad_level == 4: # Makes sure that it is an actual level
                print("Goodbye, admin, off to Level", ad_level, "you go!")
                for x in range(ad_level + 1):
                    house[x][2] = True # Changes house rooms to unlocked and lit
                    house[x][3] = False
                if ad_level == 0:
                    level_0() #Goes to the specific functions for that level
                    break
                elif ad_level == 1:
                    level_1()
                    break
                elif ad_level == 2:
                    level_2()
                    break
                elif ad_level == 3:
                    level_3()
                    break
                elif ad_level == 4:
                    level_4()
                    break
                else:
                    print("That isn't a valid level try again!")
            else:
                print("Unfortunately, that level dosen't exist. Please try again!")

    def game(): #Function for the main game itself
        global is_admin, room, house, puzzles, items, level_0, level_1, level_2, level_3, level_4, window #Defining global variables to be used thorughout the program
        is_admin = False #This will become true, if the user is found to be an admin in admin mode
        room = "" # Plcaeholder value
        house = [
            ["entrance_room",
             "The entrance room is damp, smells of wet wood, with a singular candle hung in the far corner.",
             True, False],  # Defining the rooms, the description, whether it is lit, and whether it is locked
            ["living_room",
             "In the living room, there is a fossilised sofa, and intricate designs have been created by cobwebs.", False,
             True],
            ["kitchen", "In the kitchen, there's ancient pizza on the counter, poisoning the room with its rotten stentch.",
             False, True],
            ["parlour",
             "The abandoned French parlour, frozen in time for three centuries, retains its opulent furnishings and fading grandeur, echoing whispers of bygone elegance amidst layers of dust and cobwebs.",
             False, True],
            ["attic",
             "In the dim light of a forgotten era, the 17th-century French attic harbors relics of a bygone aristocratic life: weathered trunks, moth-eaten tapestries draped over antique furniture, and the soft whispers of history lingering in the dust-laden air.",
             False, True]]
        puzzles = ["""There is a message by the door saying:
    Go where my hatred burned (literally), in my living room (the door to the north), if you dare, attached is the key
    To recieve light in the living room, solve answer this question:
    In which continent were the Napoleonic Wars fought in?
    A - Europe
    B - Asia
    C - North America""", #Defining all the puzzles in this list
                   """The key is wrapped in a message saying:
    Go forth, into the kitchen, and find the Key of Freedom in the heater of baguettes (if you dare), enclosed is the Key of Loathing
    To recieve light in the kitchen answer this question:
    Which country did Admiral Nelson fight for?
        A(Default) - The United States of America
        B - The (at that time known as) United Kingdom of Great Britain and Ireland
        C - The (at that time known as) First French Empire""",
                   """The key is wrapped in a message saying:
    Go forth, into the parlour, and find the Key of Revenge on the place which is a versatile piece of furniture, designed for comfort and support (if you dare), enclosed is the Key of Freedom
    To recieve light in the parlour answer this question
    During Napoleon Bonaparte's rise to power in France, which significant event solidified his authority and established him as the dominant figure in French politics?
        A(Default) - The Napoleonic Wars
        B - The Reign of Terror
        C -  The Coup of 18 Brumaire""",
                   """The key is wrapped in a message saying:
    Go forth, into the attic, and find the Key of Deliverance on the place which n a place where whispers of history is stitched in threads and its shadows hint at tales (if you dare), enclosed is the Key of Revenge
    To recieve light in the attic answer this question:
    What was the primary motivation behind Napoleon's decision to invade Russia in 1812?
        A(Default) - To enforce the Continental System and cripple British trade.
        B - To spread the ideals of the French Revolution across Europe.
        C -  To punish Russia for withdrawing from the Continental System."""]
        items = [["Key of Loathing", "living_room", False, 0],
                 ["Key of Freedom", "kitchen", False, 1], #Keeping tabs on all of the items in this list
                 ["Key of Revenge", "parlour", False, 2],
                 ["Key of Deliverance", "attic", False, 3]]

        def review_keys(): #Function for dropping keys and seeing which keys you have
            global room, items, name
            endloop = False
            nums = []
            print("Hi", name,
                  "welcome to your item review, here are the items you have with their corresponding item number.")
            for x in items:
                if x[2] == True:
                    print(x[0], ",", x[3])
                    nums.append(str(x[3])) #Appends the item number into a list called nums
                else:
                    pass
            option = input("Are there any items that you wish to drop. (y/n, default)")
            if option == "y":
                while 0 == 0:
                    option = input("Enter the number of the item that you wish to drop.")
                    for y in nums:
                        if y == option:
                            endloop = True #A varibale that determines whether the loop should be ended
                        else:
                            pass
                    if endloop == True:
                        break
                    else:
                        pass
                    print("Unfortunately that must have been the wrong number. Try again.")
                for z in items:
                    if z[3] == int(y):
                        z[2] = False #Changes the item varibales to false for it being found and updates wich room the item is now in
                        z[1] = room
                    else:
                        pass
                print("All right the item has been dropped, let's get back to the game.")
            else:
                print("OK, let's get back to the game!")

        def intro():  # The games introduction function
            global name
            print("Welcome to the Temple of Doom.")
            name = input("Please enter your Horror Games People ID username")
            if name == "omegabetaalphagammaraY":  # Secret admin code, in case you need to skip levels
                admin()
            else:
                pass
            print("This game is presented by the Horror Games People Industries!")
            print(
                "Certain elements of this game like descriptions, have been produced through AI models belonging to OpenAI.")
            print("2024 © Copyright Horror Games People Industries")
            print("Starting game...")
            print("Hello", name,
                  "immerse yourself in the Temple of Doom, i.e. a temple found buried under London, that the British Government wants you to explore.")
            option = input("""Please choose what to do:
        0(Default) - Yes! Let's go, I like exploring!
        1 - I'm too scared, hire someone else, I am not opening that door""")
            if option == "1":
                print("""GAME OVER!
        I mean, you can't really play without entering the temple!""")
                sys.exit(1) #Ends the program
            else:
                print("""
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ─██████──────────██████─██████████████─██████─────────██████████████─██████████████─██████──────────██████─██████████████────██████████████─██████████████─
    ─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██────██░░░░░░░░░░██─██░░░░░░░░░░██─
    ─██░░██──────────██░░██─██░░██████████─██░░██─────────██░░██████████─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██████████────██████░░██████─██░░██████░░██─
    ─██░░██──────────██░░██─██░░██─────────██░░██─────────██░░██─────────██░░██──██░░██─██░░██████░░██████░░██─██░░██────────────────██░░██─────██░░██──██░░██─
    ─██░░██──██████──██░░██─██░░██████████─██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██──██░░██─██░░██████████────────██░░██─────██░░██──██░░██─
    ─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██────────██░░██─────██░░██──██░░██─
    ─██░░██──██░░██──██░░██─██░░██████████─██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██████──██░░██─██░░██████████────────██░░██─────██░░██──██░░██─
    ─██░░██████░░██████░░██─██░░██─────────██░░██─────────██░░██─────────██░░██──██░░██─██░░██──────────██░░██─██░░██────────────────██░░██─────██░░██──██░░██─
    ─██░░░░░░░░░░░░░░░░░░██─██░░██████████─██░░██████████─██░░██████████─██░░██████░░██─██░░██──────────██░░██─██░░██████████────────██░░██─────██░░██████░░██─
    ─██░░██████░░██████░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░██────────██░░██─────██░░░░░░░░░░██─
    ─██████──██████──██████─██████████████─██████████████─██████████████─██████████████─██████──────────██████─██████████████────────██████─────██████████████─
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ─████████──████████─██████████████─██████──██████─████████████████──────████████████───██████████████─██████████████─██████──────────██████─
    ─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─
    ─████░░██──██░░████─██░░██████░░██─██░░██──██░░██─██░░████████░░██──────██░░████░░░░██─██░░██████░░██─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─
    ───██░░░░██░░░░██───██░░██──██░░██─██░░██──██░░██─██░░██────██░░██──────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██████░░██████░░██─
    ───████░░░░░░████───██░░██──██░░██─██░░██──██░░██─██░░████████░░██──────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─
    ─────████░░████─────██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─
    ───────██░░██───────██░░██──██░░██─██░░██──██░░██─██░░██████░░████──────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██──██████──██░░██─
    ───────██░░██───────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██──────────██░░██─
    ───────██░░██───────██░░██████░░██─██░░██████░░██─██░░██──██░░██████────██░░████░░░░██─██░░██████░░██─██░░██████░░██─██░░██──────────██░░██─
    ───────██░░██───────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──────────██░░██─
    ───────██████───────██████████████─██████████████─██████──██████████────████████████───██████████████─██████████████─██████──────────██████─
    ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                """) #ASCII art
                print("You have opened the rickety door, prepare to be immersed in a new world!")
                level_0()

        def level_0():
            global house, puzzles, items, room  # Allowing the function to access the global variables
            room = "entrance_room"
            print(house[0][1])
            print(puzzles[0])
            house[1][3] = False
            while 0 == 0:
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
                elif option == "admin":
                    if is_admin == True:
                        admin()
                    else:
                        print("Alright into the darkness we go.")
                    break
                else:
                    print("Onwards we go into complete darkness!")
                    break
            level_1()

        def level_1():
            global house, puzzles, items, room  # Allowing the function to access the global variables
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
                print(house[1][1])  # Description for the living room
                while 0 == 0:
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
                while 0 == 0:
                    option = input("""I have narrowed down the location of the Key of Loathing to three places
        Please choose the one you think it is:
        0(Default) -  Next to the window
        1 - In the hole in the wall
        2 - In the bookcase""")
                    if option == "2":
                        print("Yes, you've found it!")
                        items[0][2] = True
                        break
                    else:
                        print("Nope, not here, please try again!")
                house[2][3] = False
                print(puzzles[1])
                while 0 == 0:
                    option = input("""Chosee what to do:
        0(Default) - Enter the kitchen without light
        1 - Select Option A
        2 - Select Option B
        3 - Select Option C""")
                    if option == "2":
                        print("Well done, we got it right, let's go through to the kitchen.")
                        house[2][2] = True
                        break
                    elif option == "1" or option == "3":
                        print("Nope, that's wrong, we better try again.")
                    elif option == "admin":
                        if is_admin == True:
                            admin()
                        else:
                            print("Alright into the darkness we go.")
                        break
                    else:
                        print("Alright into the darkness we go.")
                        break
                level_2()

        def level_2():
            global house, puzzles, items, room, name  # Allowing the function to access the global variables
            room = "kitchen"
            if house[2][2] == False:
                option = input("""Aargh! There's no light, it's too dark!!! What should you do?:
        0(default) - Return to the living room.
        1 - Wait in the darkness for something to come and kill us""")
                if option == "1":
                    print("GAME OVER! I could have told you how you died, but it TOO DARK!!!")
                    sys.exit(1)
                else:
                    print("Phew, let's go back to the living room and restart the level!")
                    level_1()
            else:
                print(house[2][1])
                print("Carrying items UNLOCKED.")
                print(name, """you have now unlocked the ability to carry items.
        Whenever you have to enter something, entering 'item' will allow you to review the items you are carrying, and whether you want to drop them.""")
                while 0 == 0:
                    option = input("""I have narrowed down the location of the Key of Freedom to three places
        Please choose the one you think it is:
        0 -  Inside the dusty toaster
        1(Default) - Inside the ashes of the oven
        2 - In the sink""")
                    if option == "0":
                        print("Yes, you've found it!")
                        items[1][2] = True
                        break
                    elif option == "item":
                        review_keys()
                    else:
                        print("Nope, not here, please try again!")
                house[3][3] = False
                print(puzzles[2])
                while 0 == 0:
                    option = input("""Chosee what to do:
        0(Default) - Enter the parlour without light
        1 - Select Option A
        2 - Select Option B
        3 - Select Option C""")
                    if option == "3":
                        print("Well done, we got it right, let's go through to the parlour.")
                        house[3][2] = True
                        break
                    elif option == "1" or option == "2":
                        print("Nope, that's wrong, we better try again.")
                    elif option == "item":
                        review_keys()
                    elif option == "admin":
                        if is_admin == True:
                            admin()
                        else:
                            print("Alright into the darkness we go.")
                        break
                    else:
                        print("Alright into the darkness we go.")
                        break
                level_3()

        def level_3():
            global house, puzzles, items, room, name  # Allowing the function to access the global variables
            room = "parlour"
            if house[3][2] == False:
                option = input("""Aargh! There's no light, it's too dark!!! What should you do?:
        0(default) - Return to the kitchen.
        1 - Wait in the darkness for something to come and kill us""")
                if option == "1":
                    print("GAME OVER! I could have told you how you died, but it TOO DARK!!!")
                    sys.exit(1)
                else:
                    print("Phew, let's go back to the kitchen and restart the level!")
                    level_2()
            else:
                print(house[3][1])
                while 0 == 0:
                    option = input("""I have narrowed down the location of the Key of Revenge to three places
        Please choose the one you think it is:
        0 -  On a chair
        1(Default) - In the fireplace
        2 - In those annoying gaps in the sofa""")
                    if option == "0":
                        print("Yes, you've found it!")
                        items[2][2] = True
                        break
                    elif option == "item":
                        review_keys()
                    else:
                        print("Nope, not here, please try again!")
                house[4][3] = False
                print(puzzles[3])
                while 0 == 0:
                    option = input("""Chosee what to do:
            0(Default) - Enter the attic without light
            1 - Select Option A
            2 - Select Option B
            3 - Select Option C""")
                    if option == "1":
                        print("Well done, we got it right, let's go through to the parlour.")
                        house[4][2] = True
                        break
                    elif option == "2" or option == "3":
                        print("Nope, that's wrong, we better try again.")
                    elif option == "item":
                        review_keys()
                    elif option == "admin":
                        if is_admin == True:
                            admin()
                        else:
                            print("Alright into the darkness we go.")
                            break
                    else:
                        print("Alright into the darkness we go.")
                        break
                level_4()

        def level_4():
            global house, puzzles, items, room, name  # Allowing the function to access the global variables
            room = "attic"
            if house[4][2] == False:
                option = input("""Aargh! There's no light, it's too dark!!! What should you do?:
        0(default) - Return to the parlour.
        1 - Wait in the darkness for something to come and kill us""")
                if option == "1":
                    print("GAME OVER! I could have told you how you died, but it TOO DARK!!!")
                    sys.exit(1)
                else:
                    print("Phew, let's go back to the parlour and restart the level!")
                    level_3()
            else:
                print(house[4][1])
                while 0 == 0:
                    option = input("""I have narrowed down the location of the Key of Deliverance to three places
            Please choose the one you think it is:
            0 -  In the floorboards
            1(Default) - In the random box in front of me
            2 - Wrapped in the dusty tapestries""")
                    if option == "2":
                        print("Yes, you've found it!")
                        items[3][2] = True
                        break
                    elif option == "item":
                        review_keys()
                    else:
                        print("Nope, not here, please try again!")
                print("Wait, what something just came out of the wall...")
                time.sleep(2)
                ghostsarehere()

        def ghostsarehere():
            global window
            window = Tk() #Defining the tkinter window
            window.geometry("400x200") #Setting its size
            window.title("PANIC!!!") #Setting the title
            label = Label(window, text="Ghosts! I can see them! They're gonna kill us!") #Creating a text label and buttons to go on it
            label.pack()
            click_it = Button(text="Let's get them!!!", command=window.destroy) #Deystroys the tkinter window if this button is selected
            click_it.place(x=50, y=50)
            dont_click_it = Button(text="Too scary, get me out of here! I hate ghosts!!!", command=ghost_quitters) #Goes to the gost_quitters function if this button is selected
            dont_click_it.place(x=50, y=100)
            window.mainloop()
            the_end_is_here()

        def the_end_is_here():
            print("HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLP")
            print("The ghosts have tied me up with a rope.")
            option = input("""Do something:
        1 - Fight the good old-fashioned way, pick up the sword on the wall and fight like yout life depends on it, cause it probably does.
        2 - Actually I prefer the old bayonet
        3(default) - Weapons, never heard of em', I can take care of this with my bare hands!""")
            if option == "1":
                print("CLANG! That is the sound of the sword going through the ghosts and hitting the wall.")
            elif option == "2":
                print("CRASH! That is the sound of your bullet going through their hearts.")
            else:
                print("CRASH! That is the sound of you crashing into the wall after running through the ghost.")
            print("Well that ended nicely didn't it. Now we are both tied up in this attic.")
            print("""SHUSH! The ghosts are saying something:
        We are the loyal generals of Emperor Napolean, centuries ago us and our master were thrown in here by the British Government.
        Though they soon forgot those places existed, we are bound to this house by their magic until Napolean is freed.
        They left the four keys to this otherwise unbreakable cell around the house, guraded in layers of magic, meaning only mortals could move them from their places.
        The messages were a trick that you had fallen into, and now Napolean shall rule the world!""")
            print(
                "And it seems that all the keys we had worked so hard for are flying to the air straight towards these ghosst.")
            print("They combine the four keys together into the shape of a square, using the interlocking grooves.")
            print(
                "Ancient magic is awakened again, vibrations are sent throughout the entirre universe. Oh no, othe rpeople must be noticing in the outsidde world too.")
            print("""Suddeenly the ghosts utter the words:
        Libera iustum mundi imperatorem, imperatorem nostrum Napoleonem
    Which seems to be Latin for free the emperor of the world, free our Emperor Napolean.""")
            print(
                "A rip in the universe is created right in front of you, and out walks a malevolent ghost. Emperor Napolean.")
            print("""Napolean says:
        Muahahaha!
        Behold, mortals! The tides of time have bent to my will, and I, Emperor Napoleon Bonaparte, stride once more upon the earthly stage. Three centuries hence, my bones have stirred, my spirit rekindled.

        The sun quivers, the moon cowers, and the very stars tremble in my presence. The echoes of cannon fire still resonate in my ears, and the scent of victory lingers like a phantom perfume.

        The map of Europe unfurls before me, its borders mere lines drawn by trembling hands. Kings and queens, beware! Your thrones are but cushions for my weary feet.

        To the ghosts of Waterloo, I say: "Fear not, my old adversaries. I return not for vengeance, but for conquest!"

        My sword, once dulled by time, now gleams anew. My tricorn hat casts shadows across empires. The whispers of generals long gone guide my steps.

        And as I ascend the gilded steps of destiny, I declare:

        "Vive l'Empereur!"

        Hear it, ye peasants! Tremble, ye monarchs! For the Corsican Ogre has awakened, and the world shall quake beneath my boot.

       HAHAHAHAHA!
    """)
            print("""
                  8''''8 eeeee eeeee eeeeeee    e   e eeeee eeeee    eeeee eeeee  eeeee  e  ee   e eeee eeeee
                  8e   8 8  88 8  88 8  8  8    8   8 8   8 8   "    8   8 8   8  8   8  8  88   8 8    8   8
                  88   8 8   8 8   8 8e 8  8    8eee8 8eee8 8eeee    8eee8 8eee8e 8eee8e 8e 88  e8 8eee 8e  8
                  88   8 8   8 8   8 88 8  8    88  8 88  8    88    88  8 88   8 88   8 88  8  8  88   88  8
                  88eee8 8eee8 8eee8 88 8  8    88  8 88  8 8ee88    88  8 88   8 88   8 88  8ee8  88ee 88ee8
                  """) #ASCII art
            unamehalloffame()

        def ghost_quitters():
            global window
            window.destroy() #Deystorys the tkinter window
            print("GAME OVER!!! You quit, you lose!")
            sys.exit(1)

        def unamehalloffame():
            global name
            print("Your username is being added to the username hall of fame for getting to the end.")
            print("Sorry, but you had to lose, so nobdy could beat this game.")
            print("The ghosts were invincible, or where they, version 4 landing soon!")
            if name == "omegabetaalphagammaraY":
                print("Dear admin, please customize your username before it is put onto the hall of fame.")
                name = input("Customize your username here, admin.")
            else:
                pass
            print("The big username hall of fame, including you username, below:")
            uname = open("halloffame.txt", "a") #Opens the file in appending mode
            uname.write(name) #Appends the usernmae into the file
            uname.close() # Closes the file
            uname = open("halloffame.txt", "r") # Opens the file in reading mode
            print(uname.read())
            print("Well done for getting to the end but....")
            print("GAME OVER!, sorry you lost to Napolean, stay tuned for version 4!")
            sys.exit(1)

        intro()#Calls the introduction function for the start


    game() # Calls the main game function

 except: #This is carried out if there is a bug in the game
     print("I apolgize, but there has been an error in the game...")
     print("Please report this error to Horror Games People Industries.")
     print("Take a screenshot and tag us on X!")
     print("I am afraid its GAME OVER! Please hold on while we resolve the problem...")
     sys.exit(1)