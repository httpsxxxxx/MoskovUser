print("Hello user, Welcome to my rock paper scissors game")

import os
import sys
import random

os.system('clear')

ask = input("Would you like to play?[y/n]: ")

while ask == "":
	print("Please enter something")
	ask = input("Would you like to play?[y/n]: ")
if ask == "n" or ask == "N":
	print("bye")
	sys.exit()
else:
	print("Lets proceed")

def statements(If, Elif):
	if bot == str(If):
		print("bot won")
	elif bot == str(Elif):
		print("Tie")
	else:
		print("You won")

while True:
	play = input("What is your attack [rock, paper. scissors q to quit]?: ")
	if play == "q":
		break

	attacks = ["rock", "paper", "scissors"]
	bot = random.choice(attacks)

	if play == "rock" or play == "Rock":
		statements("paper", "rock")
	elif play == "paper" or play == "Paper":
		statements("scissors", "paper")
	elif play == "scissors" or play == "Scissors":
		statements("rock", "scissors")
	elif play == "clear":
		os.system('clear')
	else:
		print("You deadass")
		break
