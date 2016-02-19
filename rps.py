#Case Study 1: The Rock-Paper-Scissors Game
#CIS 473
#Authors: Alberto Rivera, Lakshay Khatter

from random import randint
import os

rock = 1
paper = 2
scissors = 3

def main():
	usermove =  get_usermove()
	while (usermove != 0):
		compmove = get_compmove()
		get_winner(usermove, compmove)
		usermove = get_usermove()


		os.system('cls' if os.name == 'nt' else 'clear')
	print("THANKS FOR PLAYING!")
	return 0


def get_usermove():
	print("Enter 1 (rock), 2 (paper), 3(scissors) or 0 to Exit")
	usrinput = -1
	try:
		usrinput = int(raw_input())
	except:
		print("Invalid Input. Try Again")
		get_usermove()
	if ( not( 0 <= usrinput <= 3)):
		print("Invalid Input. Try Again")
		get_usermove()
	return usrinput

def get_compmove():
	return randint(1,3)

def get_winner(usrmv, cmpmove):

	if (usrmv == cmpmove):
		print("TIE!")
	elif (usrmv == rock and cmpmove == paper):
		print("You Lose!")
	elif (usrmv == rock and cmpmove ==  scissors):
		print("You Win!")
	elif (usrmv == paper and cmpmove == scissors):
		print("You Lose!")
	elif (usrmv == paper and cmpmove == rock):
		print("You Win!")
	elif (usrmv == scissors and cmpmove == rock):
		print("You Lose!")
	elif (usrmv == scissors and cmpmove == paper):
		print("You Win!")

	#code should not get here
	#print("No Winner??????")

main()