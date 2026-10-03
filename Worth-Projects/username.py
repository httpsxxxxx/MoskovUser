#Working username login
import time
import os

def clear():
    os.system('clear')
clear()

input("enter!")

def sleep():
    time.sleep(2)

print("Hello human, this is an username thingy")
print("There are a few rules for setting your own username")
print("""
1. 12 chracters only
2. No spaces
3. No digits
""")
time.sleep(5)
print("If that is okay to you lets go proceed")
sleep()
clear()

x = input("Would you like to count your expected username? (y/N): ")
clear()

if x == "y":
    y = input("enter the username: ")
    print(f"The length chracters of that username is {len(y)}")
    time.sleep(5)

elif x == "Y":
    y = input("enter the username: ")
    print(f"The length chracters of that username is {len(y)}")
    time.sleep(5) 
else:
    print("ok proceed!")
    sleep()
clear()

inputting = input("enter your username:")

if len(inputting) <= 12:
    print("username verified")
    sleep()
    if inputting.find(" ") == -1:
        print("no spaces verified")
        sleep()
        if inputting.isdigit():
            print("Something went wrong, please try again and read the rules")
        else:
            print("no digits verified")
            sleep()
            clear()
            print(f"Welcome here {inputting}")
    else:
        print("Something went wrong, please try again and read the rules")
else:
    print("Something went wrong, please try again and read the rules")
