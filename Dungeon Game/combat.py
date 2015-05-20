import random

class Combat:
	dodgeLimit = 6
	attackLimit = 6
	
	#randomly check if the entity can dodge/attack
	def dodge(self):
		roll = random.randint(1, dodgeLimit)
		return roll > 4
		
	def attack(self):
		roll = random.randint(1, attackLimit)
		return roll > 4