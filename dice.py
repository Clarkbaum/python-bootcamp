import random

class Dice:
	def roll(self):
		return random.randint(1,10), random.randint(1,10)

dice = Dice()
print(dice.roll())
