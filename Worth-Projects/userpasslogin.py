#Working username and password login
import os
import time

def clear():
    os.system('clear')
def sleep():
    time.sleep(2)
def blank():
    print("\n")
clear()

print(" Hello user please sign up for an account ")
print("|----------------------------------------|")
blank()

print("""
Notice: Please make sure your username and password has
only 8 chracters you may mix it with a number thanks!
""")
blank()



username = input("Enter your username: ")

while len(username) > 8:
    print(f"your username is {username}...")
    print("something went wrong please follow the notes rule")
    sleep()
    clear()
    username = input("Enter your username: ")
print(f"your username is {username}...")
sleep()
print("username verified!")
blank()

password = input("Enter your password: ")

while len(password) > 8:
    print(f"your password is {password}...")
    print("something went wrong please follow the notes rule")
    sleep()
    clear()
    password = input("Enter your password: ")
censor = password[-3:]
print(f"your password is *****{censor}")
sleep()
print("password verified!")

