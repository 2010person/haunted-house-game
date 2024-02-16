import sys # Default module so you should have it 
import part_1_the_beginning as p1 # Imported the part 1 python file as "p1"
try: 
    p1.intro() # Called the intro() function from the part 1 python file
    print("As this game is still in development, you have reached the END.")
    def review_keys():
        items = p1.items
        print("These are the keys you have, with therir item number:")
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
                    pass
        else:
            print("OK, back you go.")

except:
    print("I apolgize, but there has been an error in the game...")
    print("Please report this error to Horror Games People Industries.")
    print("Take a screenshot and tag us on X!")
    print("I am afraid its GAME OVER! Please hold on while we resolve the problem...")
    sys.exit(1)
