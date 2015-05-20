from character import Character
from monsters import Dragon, Goblin, Troll

class Game:
	#setup the gamne
	def setup(self):
		self.player = Character()
		self monsters = [
			Goblin(),
			Troll(),
			Dragon()
		]
		self.monster = self.getNextMonster()
	
	#get the next monster on the monster list
	def getNextMonster(self):
		try:
			return self.monsters.pop(0)
		except IndexError:
			return None
	
	def monsterTurn(self):
	
	def playerTurn(self):
		
	def cleanup(self):
	
	#overwrite initializing function	
	def __init__(self):
		self.setup()
		
		#run monster/player turns till one of them dies
		while self.player.HP and (self.monster or self.monsters):
			print(self.player)
			self.monsterTurn()
			self.playerTurn()
			self.cleanup()
		
		if self.player.HP:
			print("You win!")
		elif self.monster or self.monsters:
			print("You lose!")
			