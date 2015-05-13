import random

CELLS = [(0,0), (0,1), (0,2),
		 (1,0), (1,1), (1,2),
		 (2,0), (2,1), (2,2)]

def getLocations():
	#monster = random
	#door = random
	#start = random
	
	return monster, door, start
	
def movePlayer(player, move):
	
	
#main
print("Welcome to the dungeon!")
while True:
	print("You're currently in room {}") #fill in with player position
	print("You can move {}") # fill in with moves
	print("Enter QUIT to exit the game.")
	
	move = input("> ")
	move = move.upper()
	
	if move == 'QUIT':
		break
	
	