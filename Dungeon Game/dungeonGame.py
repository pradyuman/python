import random
import monsters

#map of the dungeon
CELLS = [(0,0), (0,1), (0,2), (0,3),
		 (1,0), (1,1), (1,2), (1,3),
		 (2,0), (2,1), (2,2), (2,3),
		 (3,0), (3,1), (3,2), (3,3)]

#get locations that the player can go to
def getLocations():
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	start = random.choice(CELLS)
	
	#if the coordiates of any of the entities overlap, redo the process
	if monster == door or monster == start or door == start:
		return getLocations()
	
	return monster, door, start
	
def movePlayer(player, move):
	#player is a tuple of y,x coordinates
	y, x = player
	
	if move == 'LEFT':
		x -= 1
	elif move == 'RIGHT':
		x += 1
	elif move == 'UP':
		y -= 1
	elif move == 'DOWN':
		y += 1
	
	#return player	
	return y, x

#get moves that the player can go to
#removes the moves in which the player will go out of the dungeon boundaries
def getMoves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	#player is a tuple of y,x coordinates
	if player[1] == 0:
		moves.remove('LEFT')
	if player[1] == 3:
		moves.remove('RIGHT')
	if player[0] == 0:
		moves.remove('UP')
	if player[0] == 3:
		moves.remove('DOWN')
	return moves

#visual map of the dungeon
def drawMap(player):
	tile = '|{}'
	for i, cell in enumerate(CELLS):
		#this is the right most column (needs different formatting)
		if i in [3, 7, 11, 15]:
			#if the cell is the player, print an 'X' to mark the player
			if cell == player:
				print(tile.format('X|'))
			else:
				print(tile.format('_|'))
		#all the other columns
		else:
			#if the cell is the player, print an 'X' to mark the player
			if cell == player:
				print(tile.format('X'), end = '')
			else:
				print(tile.format('_'), end = '')
		
#main
#set random locations for the game entities
monster, door, player = getLocations()

print("Welcome to the dungeon!")

while True:
	moves = getMoves(player)
	
	print("You're currently in location {}".format(player))
	drawMap(player)
	print("You can move {}".format(moves))
	print("Enter QUIT to exit the game.")
	
	move = input("> ")
	move = move.upper()
	
	if move == 'QUIT':
		break
		
	if move in moves:
		player = movePlayer(player, move)
	else:
		print("ERROR: Your move is invalid. Walls are hard, don't walk into them!")
		continue
	
	if player == door:
		print("Congratulations! You escaped!")
		break
	elif player == monster:
		print("GAME OVER. You were eaten by the monster.")
		break
	
	