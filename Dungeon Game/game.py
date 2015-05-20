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
		
	def hit(self, entity, strength):
		entity.HP -= strength
	
	#get the next monster on the monster list
	def getNextMonster(self):
		try:
			return self.monsters.pop(0)
		except IndexError:
			return None
	
	#monster's turn
	def monsterTurn(self):
		if self.monster.attack():
			print("{} is attacking!").format(self.monster))
			
			if self.player.dodge():
				print("You dodge {}'s attack! Current HP: {}".format(self.monster, self.player.HP))
			else:
				hit(self.player, 1)
				print("You were hit! Remaining HP: {}".format(self.player.HP))
		else:
			print("The {} is tired. The monster cannot attack this turn.".format(self.monster))
	
	#player's turn				
	def playerTurn(self):
		playerMove = input("[A]ttack, [R]est, [Q]uit?").upper()
		
		#if player is attacking
		if playerMove == 'A':
			print("You're attacking the {}".format(self.monster))
			
			if self.player.attack():
				if self.monster.dodge():
					print("{} dodged your attack!".format(self.monster))
				else:
					if self.player.levelUp():
						hit(self.monster, 2)
					else:
						hit(self.monster, 1)
					
					print("You hit {} with your {}!".format(self.monster, self.player.weapon))
			else:
				print("Your attack missed!")
		elif playerMove == 'R':
			self.player.rest()
		elif playerMove == 'Q'
			sys.exit()
		else:
			self.playerTurn()
		
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
			