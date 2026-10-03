#Rock Paper Scissors Game
import os
import sys
import random
os.system('clear')

hack = random.randint(1, 3)
print(str(hack) + ' debug')
if hack == 1:
    print("Rock")
elif hack == 2:
    print("Paper")
elif hack == 3:
    print("Scissors")
else:
    print("WHat?")