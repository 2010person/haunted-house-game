import sys # Default module so you should have it 
import part_1_the_beginning as p1 # Imported the part 1 python file as "p1"
try: 
    p1.intro() # Called the intro() function from the part 1 python file
    print("As this game is still in development, you have reached the END.")
                
except:
    print("I apolgize, but there has been an error in the game...")
    print("Please report this error to Horror Games People Industries.")
    print("Take a screenshot and tag us on X!")
    print("I am afraid its GAME OVER! Please hold on while we resolve the problem...")
    sys.exit(1)
