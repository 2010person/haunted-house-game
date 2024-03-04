import sys # Default module, so you should have it, unless it was deleted 
import admin_command as ad # Imports the admin command python code as "ad"
import tkinter as tk
from tkinter import PhotoImage

#try:
class Window:
    def __init__(self, image):
        self.image = image
        self.root = tk.Tk()
        self.widgets()
        self.root.mainloop()
    def widgets(self):
        self.img = PhotoImage(file=self.image)
        label = tk.Label(self.root, image=self.img)
        label.pack()

admin = False
room = ""
house = [["entrance_room", "The entrance room is damp, smells of wet wood, with a singular candle hung in the far corner.", True, False], # Defining the rooms, the description, whether it is lit, and whether it is locked 
        ["living_room", "In the living room, there is a fossilised sofa, and intricate designs have been created by cobwebs.", False, True],
        ["kitchen", "In the kitchen, there's ancient pizza on the counter, poisoning the room with its rotten stentch.", False, True],
        ["parlour", "The abandoned French parlour, frozen in time for three centuries, retains its opulent furnishings and fading grandeur, echoing whispers of bygone elegance amidst layers of dust and cobwebs.",
          False, True],
          "dining hall", "cellar"] 
puzzles = ["""There is a message by the door saying:
Go where my hatred burned (literally), in my living room (the door to the north), if you dare, attached is the key
To recieve light in the living room, solve answer this question:
In which continent were the Napoleonic Wars fought in?
A - Europe
B - Asia
C - North America""",
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
items = [["Key of Loathing", "living_room", False],
        ["Key of Freedom", "kitchen", False],
        ["Key of Revenge", "parlour", False],
        ["Key of Deliverance", "attic", False]]
def review_keys():
    global room, items
    num = 0
    print("These are the keys you have, with their item number:")
    for x in range(len(items)):
        if items[x][2] == False:
            pass
        else:
            num = num + 1
            print(items[x][0], num)
            exec(f"copy_item_name_{num} = items[x][0]")
    option = input("Are there any you wish to drop y / n(default)?")
    if option == "y":
        while 0==0:
            option = input("Please enter the item number of the item you wish to drop.")
            if "copy_item_name_" + option in locals():
                for x in items:
                    for y in x:
                        if y == (f"copy_item_name_{num}"):
                            posistion = x
                        else:
                            pass
                break
            else:
                print("Sorry but that is not a valid item number. Please try again.")
        items[posistion][2] = False
        print("Alright", items[posistion][0], "has now been dropped, let's get back to the question!")
        items[posistion][1] = room
    else:
        print("OK, back you go.")
def intro(): # The games introduction function
    global name
    print("Welcome to the Temple of Doom.")
    name = input("Please enter your Horror Games People ID username")
    if name == "omegabetaalphagammaraY": # Secret admin code, in case you need to skip levels
        ad.admin()
    else:
        pass
    print("This game is presented by the Horror Games People Industries!")
    print("Certain elements of this game like images and descriptions, have been produced through AI models belonging to OpenAI.")
    print("2024 © Copyright Horror Games People Industries")
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
        """)
        print("You have opened the rickety door, prepare to be immersed in a new world!")

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
        elif option == "admin":
            if admin == True:
                ad.admin()
            else:
                print("Alright into the darkness we go.")
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
                items[0][2] = True
                break
            else:
                print("Nope, not here, please try again!")
        house[2][3] = False
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
            elif option == "admin":
                if admin == True:
                    ad.admin()
                else:
                    print("Alright into the darkness we go.")
                break
            else:
                print("Alright into the darkness we go.")
                break
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
            print("Phew, let's go back to the living room and restart the level!")
            level_1()
    else:
        print(house[2][1])
        print("Carrying items UNLOCKED.")
        print(name, """you have now unlocked the ability to carry items. 
Whenever you have to enter something, entering 'item' will allow you to review the items you are carrying, and whether you want to drop them.""")
        while 0==0:
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
        while 0==0:
            option = input("""Chosee what to do:
0(Default) - Enter the kitchen without light
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
                if admin == True:
                    ad.admin()
                else:
                    print("Alright into the darkness we go.")
                break
            else:
                print("Alright into the darkness we go.")
                break
        level_3()

    
def level_3():
    global house, puzzles, items, room, name # Allowing the function to access the global variables
    room = "parlour"
    if house[3][2] == False:
        option = input("""Aargh! There's no light, it's too dark!!! What should you do?:
0(default) - Return to the living room.
1 - Wait in the darkness for something to come and kill us""")
        if option == "1":
            print("GAME OVER! I could have told you how you died, but it TOO DARK!!!")
            sys.exit(1)
        else:
            print("Phew, let's go back to the kitchen and restart the level!")
            level_2()
    else:
        print(house[3][1])
        while 0==0:
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
        

def level_4():
    pass

def test():
    image = "/workspaces/haunted-house-game/ghosts.png"
    Window(image)

test()

#except:
 #   print("I apolgize, but there has been an error in the game...")
  #  print("Please report this error to Horror Games People Industries.")
   # print("Take a screenshot and tag us on X!")
    #print("I am afraid its GAME OVER! Please hold on while we resolve the problem...")
    #sys.exit(1)
