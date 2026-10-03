#School Simplified form
import os

os.system("clear")

print("==========Student Form==========")
print()
print("=====Input=====")

Name = input("Full name: ")
Age = int(input("Age: "))
Grade = int(input("Grade: "))
Section = input("Section: ")
Gender = input("Gender: ")
print()

print("=====Output=====")
print("Your full name is " + Name)
print("Your Age is " + str(Age))
print("Your Grade & Section is " + str(Grade) + " - " + Section)
print("Your Gender is a " + Gender)

