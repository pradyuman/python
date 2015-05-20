import random
from combat import Combat

#Possible colors for monsters
COLORS = ['yellow', 'red', 'blue', 'green']

#a monster is a combat entity
class Monster(Combat):
	#Hit Points
	minHP = 1
	maxHP = 1
	
	#Experience Points
	minXP = 1
	maxXP = 1
	
	#Other attributes
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
class Goblin(Monster):
	maxHP = 3
	maxXP = 2
	sound = 'squeak'

#Troll subclass
class Troll(Monster):
	minHP = 3
	maxHP = 5
	minXP = 2
	maxXP = 6
	sound = 'growl'
	
#Dragon subclass
class Dragon(Monster):
	minHP = 5
	maxHP = 10
	minXP = 6
	maxXP = 10
	sound = 'rooooooooaaaaaaaar'
	