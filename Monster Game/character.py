import random
from combat import Combat

#a character is a combat entity
class Character(Combat):
	XP = 0 #experience
	baseHP = 10 # hit points
	
	#overwriting Combat attributes/methods to give character the upper hand against monsters
	attack_limit = 10
	def attack(self):
		roll = random.randint(1, self.attack_limit)
		if self.weapon == 'sword':
			roll += 1
		elif self.weapon == 'axe':
			roll += 2
		#now the player is more likely to attack (max is 10 so the attack probability is higher)
		return roll > 4
	
	def __init__(self, **kwargs):
		#setting base attributes
		self.name = input("Name: ")
		self.weapon = self.getWeapon()
		self.HP = self.baseHP
		
		for key, value in kwargs.items():
			setattr(self, key, value)
	
	#formatting string output
	def __str__(self):
		return '{}, HP: {}, XP: {}'.format(self.name, self.HP, self.XP)
		
	def rest(self):
		if self.HP < self.baseHP:
			self.HP += 1
		
	def levelUp(self):
		return self.XP >= 5
	
	#ask player for weapon choice
	def getWeapon(self):
		weaponChoice = input("Weapon ([S]word, [A]xe. [B]ow): ").upper()
		
		if weaponChoice in 'SAB':
			if weaponChoice == 'S':
				return 'sword'
			elif weaponChoice == 'A':
				return 'axe'
			elif weaponChoice == 'B':
				return 'bow'
		else:
			print("You entered a weapon that is not supported. Please try again.")
			return self.getWeapon()