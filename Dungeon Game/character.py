class Character:
	XP = 0 #experience
	HP = 10 # hit points
	
	def __init__(self, **kwargs):
		#setting base attributes
		self.name = input("Name: ")
		self.weapon = self.getWeapon()
		
		for key, value in kwargs.items():
			setattr(self, key, value)
	
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