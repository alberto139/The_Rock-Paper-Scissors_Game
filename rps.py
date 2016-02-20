#Case Study 1: The Rock-Paper-Scissors Game
#CIS 473
#Authors: Alberto Rivera, Lakshay Khatter

import random
from random import randint
import os

rock = 1
paper = 2
scissors = 3
mincount = 10 #minumin number of iterations before we use non random picks
#chain = [[0 for x in range(3)] for x in range(3)]

userwin = 0
compwin = 0


def main():


	oldusermove = 0
	count = 0
	chain = [[0 for x in range(3)] for x in range(3)]

	usermove =  get_usermove()
	while (usermove != 0):
		print("Wins: " + str(userwin) + " - Losses: " + str(compwin))
		compmove = get_compmove(chain[oldusermove-1], count)
		get_winner(usermove, compmove)
		usermove = get_usermove()
		chain = update_chain(chain, oldusermove, usermove, count)
		oldusermove = usermove
		count = count + 1

		os.system('cls' if os.name == 'nt' else 'clear')
		print(chain)
	print("THANKS FOR PLAYING!")
	return 0


def get_usermove():
	print("Enter 1 (rock), 2 (paper), 3(scissors) or 0 to Exit")
	usrinput = raw_input()
	if (usrinput != '1' and usrinput != '2' and usrinput !='3' and usrinput != '0'):
			print("Invalid input!")
			return get_usermove()
	return int(usrinput)

def get_compmove(partchain, count):

	if (count < mincount):
		return randint(1,3)
	#print("PartChain :" + str(partchain))

	problist = partchain[rock-1]*[paper] + partchain[paper-1]*[scissors] + partchain[scissors-1]*[rock]
	#print("Problist :" + str(problist))

	if len(problist) == 0:
		return [rock-1, paper-1, scissors-1]
	return random.choice(problist)

def get_winner(usrmv, cmpmove):
	global userwin
	global compwin

	if (usrmv == cmpmove):
		print("TIE!")
	elif (usrmv == rock and cmpmove == paper):
		print("You Lose!")
		compwin = compwin+1
	elif (usrmv == rock and cmpmove ==  scissors):
		print("You Win!")
		userwin = userwin + 1
	elif (usrmv == paper and cmpmove == scissors):
		print("You Lose!")
		compwin = compwin+1
	elif (usrmv == paper and cmpmove == rock):
		print("You Win!")
		userwin = userwin + 1
	elif (usrmv == scissors and cmpmove == rock):
		print("You Lose!")
		compwin = compwin+1
	elif (usrmv == scissors and cmpmove == paper):
		print("You Win!")
		userwin = userwin + 1

def update_chain(matrix, oldusrmv, usrmv, count):
	matrix[oldusrmv-1][usrmv-1] += 1
	return matrix


main()