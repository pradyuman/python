import random

#Possible colors for monsters
COLORS = ['yellow', 'red', 'blue', 'green']

#Monster class
class Monster:
	minHP = 1
	maxHP = 1
	minXP = 1
	maxXP = 1
	weapon = 'sword'
	sound = 'roar'
	
	#overwriting initialize method
	def __init__(self, **kwargs):
		self.HP = random.randint(self.minHP, self.maxHP)
		self.experience = random.randint(self.minXP, self.maxXP)
		self.color = random.choice(COLORS)
		
		#in the case that keyword arguments are given
		for key, value in kwargs.items():
			setattr(self, key, value)
	
	#defining a battle cry for the monster
	def battlecry(self):
		return self.sound.upper()
		
#Goblin subclass
