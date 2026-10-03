#number guessing game
import os
import time
import sys

def func(x):
    if x == "clear":
        os.system("clear")
    elif x == "time":
        time.sleep(2)
    else:
        print("wrong bruh")
func('clear')


name = input("What is your name: " )

while name == "":
    print("Enter your name bro")
    name = input("What is your name: ")
func('clear')
print(f"Hello {name}, am thinking a number between 1 to 10. Can you guess it? Go try it out")
func('time')

RightNum = 7

for guess in reversed(range(1, 6)):
    try:
        #global x
        x = int(input(f"Take a guess ({guess} tries left): "))
        if x > 8:
            print("Too high")
        elif x < 6:
            print("Too low")
        else:
            break
    except Exception:
        print("Enter a number only")
func('clear')
if x == 7:
    print("You've guessed it congratss")
else:
    print("""Sorry you lost.
    i was thinking the number 7""")