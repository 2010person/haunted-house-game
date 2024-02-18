import sys # Default module so you should have it 
import part_1_the_beginning as p1 # Imported the part 1 python file as "p1"
#try: 
p1.intro() # Called the intro() function from the part 1 python file
print("As this game is still in development, you have reached the END.")
def review_keys():
    num = 0
    items = p1.items
    room = p1.room
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
        p1.items = items
    else:
        print("OK, back you go.")

#except:
 #   print("I apolgize, but there has been an error in the game...")
  #  print("Please report this error to Horror Games People Industries.")
   # print("Take a screenshot and tag us on X!")
    #print("I am afraid its GAME OVER! Please hold on while we resolve the problem...")
    #sys.exit(1)
