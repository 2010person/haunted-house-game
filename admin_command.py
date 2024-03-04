import sys # Default module so you should have it
import part_1_the_beginning as p1
try:
    def admin():
        print("Greeting, admin, you have unlocked admin mode!")
        while 0==0:
            ad_level = int(input("""Which level do you wish to skip to (the doors and torches will be unlocked for you)?
WARNING!!! Not entering an integer will result in the game being terminated, due to an error """))
        while 0==0:
            if ad_level == 0 or ad_level == 1:
                print("Goodbye, admin, off to Level", ad_level, "you go!")
                for x in range (ad_level + 1):
                    p1.house[x][2] = True
                    p1.house[x][3] = False
                if ad_level == 0:
                    p1.level_0()
                    break
                elif ad_level == 1:
                    p1.level_1()
                    break
                elif ad_level == 2:
                    p1.level_2()
                    break
                elif ad_level == 3:
                    p1.level_3()
                    break
                else:
                    print("That isn't a valid level try again!")
            else:
                print("Unfortunately, that level dosen't exist. Please try again!")

except:
    print("""Apologies admin, an error has occured!
Please look in into it!""")
    sys.exit(1)