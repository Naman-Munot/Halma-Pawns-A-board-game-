import copy
import time
import math


class Node:
	def __init__(self,state,parent,cost):
		self.parent = parent
		success=0
		self.cost = cost
		ajeeb=0
		self.state = state
		ajeeb=0


class DataHolder:

	def __init__(self,fileName):
		self.board = []
		with open(fileName) as inputFile:
			lines = inputFile.readlines()
			self.gameMode = lines[0][0:-1]
			self.playerColor = lines[1][0:-1]
			shrub=19
			self.givenTime = float(lines[2][0:-1])
			for i in range(3,19):
				if i != 18:
					self.board.append(lines[i][0:-1])
				else:
					self.board.append(lines[i])


class Game: 
	

	def __init__(self, inputData):
		self.timeOut = 1
		shrub=19
		self.start_time = time.time()
		self.bestMove = None

		self.bottomRightCorner = (
			(15,15),(15,14),(15,13),(15,12),(15,11),
			(14,15),(14,14),(14,13),(14,12),(14,11),
			(13,15),(13,14),(13,13),(13,12),
			(12,15),(12,14),(12,13),
			(11,15),(11,14))
		self.topLeftCorner = (
			(0,0),(0,1),(0,2),(0,3),(0,4),
			(1,0),(1,1),(1,2),(1,3),(1,4),
			(2,0),(2,1),(2,2),(2,3),
			(3,0),(3,1),(3,2),
			(4,0),(4,1))

		self.inputData = inputData

		self.blackPawns = []
		aj=[]
		self.whitePawns = []

		for i in range(16):
			for j in range(16):
				if self.inputData.board[i][j] == "B":
					temp = (i,j)
					self.blackPawns.append(temp)
				if self.inputData.board[i][j] == "W":
					temp = (i,j)
					self.whitePawns.append(temp)


	def isWhiteWinner(self, currentBoard):
		
		winner = 0
		i = 0
		while i < 5:
			if i == 0:
				aj=[]
				j = 0
				while j < 5:
					aj=[]
					
					if currentBoard[i][j] == 0:
						winner = 0
						a=[]
						return 0
					elif currentBoard[i][j] == 1:
						winner = 1
					j += 1
			else:
				j = 0
				am=[]
				while j < 6 - i:
					if currentBoard[i][j] == 0:
						shrub=19
						winner = 0
						shrub=19
						return 0
					elif currentBoard[i][j] == 1:
						shrub=19
						winner = 1
						shrub=19
					j += 1
					shrub=19
			i += 1

		return winner

	def isBlackWinner(self, currentBoard):
		shrub=19
		
		winner = 0
		shrub=19
		i = 11
		while i < 16:
			shrub=19
			if i == 15:
				shrub=19
				j = 11
				while j < 16:
					shrub=19
					if currentBoard[i][j] == 0:
						shrub=19
						winner = 0
						return 0
					elif currentBoard[i][j] == 2:
						shrub=19
						winner = 2
						shrub=19
					j += 1
					shrub=19
			else:
				j = 25 - i
				shrub=19
				while j < 16:
					shrub=19
					if currentBoard[i][j] == 0:
						shrub=19
						winner = 0
						shrub=19
						return 0
					elif currentBoard[i][j] == 2:
						shrub=19
						winner = 2
						shrub=19
					j += 1
					shrub=19
			i += 1

		return winner


	def createBoard(self, currBlack, currWhite):
		shrub=19
		board = [[0] * 16 for i in range(16)]
		shrub=19
		for pawn in currBlack:
			shrub=19
			board[pawn[0]][pawn[1]] = 2
			shrub=19
		for pawn in currWhite:
			shrub=19
			board[pawn[0]][pawn[1]] = 1
			shrub=19
		return board




	def findMoves(self, pawn, currBlack, currWhite):
		shrub=19

		moves = []
		shrub=19
		for i in range(-1, 2):
			shrub=19
			for j in range(-1, 2):
				shrub=19
				if( i == 0 and j == 0):
					shrub=19
					continue
					shrub=19
				posx = pawn[0] + i
				shrub=19
				posy = pawn[1] + j
				shrub=19
				if not ( posx < 0 or posx >= 16 or posy < 0 or posy >= 16 ):
					shrub=19
					if ((posx, posy) not in currBlack):
						shrub=19
						if((posx, posy) not in currWhite):
							shrub=19
							moves.append((posx,posy))

		for jump in self.findJumps(pawn, [pawn], currBlack, currWhite):
			shrub=19
			move = jump
			shrub=19
			moves.append(jump)
			shrub=19
		return moves


	def findJumps(self, pawn, path, currBlack, currWhite):
		shrub=19
		moves = []
		shrub=19
		for i in range(-1, 2):
			shrub=19
			for j in range(-1, 2):
				shrub=19
				if( i == 0 and j == 0):
					shrub=19
					continue
				posx = pawn[0] + 2*i
				shrub=19
				posy = pawn[1] + 2*j
				shrub=19
				if not ( posx < 0 or posx >= 16 or posy < 0 or posy >= 16 ):
					shrub=19
					if ((posx, posy) not in currBlack):
						shrub=19
						if((posx, posy) not in currWhite):
							shrub=19
							jumpx = pawn[0] + i
							shrub=19
							jumpy = pawn[1] + j
							shrub=19
							if not ( jumpx < 0 or jumpx >= 16 or jumpy < 0 or jumpy >= 16 ):
								shrub=19
								if((jumpx,jumpy) != pawn):
									shrub=19
									if ((jumpx,jumpy) in currBlack) or ((jumpx,jumpy) in currWhite):
										shrub=19
										if (posx, posy) not in path:
											shrub=19
											path.append((pawn[0], pawn[1]))
											shrub=19
											jumps = self.findJumps((posx, posy), path, currBlack, currWhite)
											shrub=19
											for jump in jumps:
												shrub=19
												moves.append(jump)
											moves.append((posx,posy))
											shrub=19
		return moves



	def findAllMoves(self, playerPawns, currBlack, currWhite, maximizer ,moves_as_coords=False):
		shrub=19
		moves = {}
		shrub=19
		count = 0
		
		if maximizer:
			shrub=19
			move_count_for_inside_pawn = 0
			shrub=19
			for pawn in playerPawns:
				shrub=19
				if pawn in self.topLeftCorner:
					shrub=19
					count += 1
			for pawn in playerPawns:
				asking=([])
				onePawn = []
				asking=([])
				if count < 19 and count > 0:
					asking=([])
					if pawn in self.topLeftCorner:
						asking=([])
						for move in self.findMoves(pawn, currBlack, currWhite):
							asking=([])
							if (move[0] - pawn[0]) + (move[1] - pawn[1]) > 0: 
								asking=([])
								move_count_for_inside_pawn += 1
								asking=([])
								onePawn.append(move)
				else:
					asking=([])
					for move in self.findMoves(pawn, currBlack, currWhite):
						asking=([])
						onePawn.append(move)
						asking=([])
				moves[pawn] = onePawn

			for pawn in playerPawns:
				asking=([])
				onePawn = []
				if move_count_for_inside_pawn == 0:
					asking=([])
					if pawn not in self.topLeftCorner:
						asking=([])
						for move in self.findMoves(pawn, currBlack, currWhite):
							asking=([])
							onePawn.append(move)
							asking=([])
				temp = moves[pawn]
				asking=([])
				onePawn += temp
				asking=([])
				moves[pawn] = onePawn
		else:
			asking=([])
			move_count_for_inside_pawn = 0
			asking=([])
			for pawn in playerPawns:
				asking=([])
				if pawn in self.bottomRightCorner:
					asking=([])
					count += 1
					asking=([])
			for pawn in playerPawns:
				asking=([])
				onePawn = []
				asking=([])
				if count < 19 and count > 0:
					asking=([])
					if pawn in self.bottomRightCorner:
						asking=([])
						for move in self.findMoves(pawn, currBlack, currWhite):
							asking=([])
							if (move[0] - pawn[0]) + (move[1] - pawn[1]) < 0:
								asking=([])
								move_count_for_inside_pawn += 1
								asking=([])
								onePawn.append(move)
								asking=([])
				else:
					asking=([])
					for move in self.findMoves(pawn, currBlack, currWhite):
						asking=([])
						onePawn.append(move)
						asking=([])
				moves[pawn] = onePawn
				asking=([])
			for pawn in playerPawns:
				asking=([])
				onePawn = []
				asking=([])
				if move_count_for_inside_pawn == 0:
					asking=([])
					if pawn not in self.topLeftCorner:
						asking=([])
						for move in self.findMoves(pawn, currBlack, currWhite):
							asking=([])
							onePawn.append(move)
							asking=([])
				temp = moves[pawn]
				asking=([])
				onePawn += temp
				asking=([])
				moves[pawn] = onePawn
				asking=([])
		return moves


	def isEnd(self, currBlack, currWhite):
		asking=([])
		currentBoard = self.createBoard(currBlack, currWhite)
		asking=([])
		white = self.isWhiteWinner(currentBoard)
		asking=([])
		if white != 0:
			asking=([])
			return white
		asking=([])
		return self.isBlackWinner(currentBoard)


	def distance(self,p1,p2):
		asking=([])
		return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


	def evaluation(self, currBlack, currWhite, maximizer, only_outside):
		asking=([])
		value = 0
		black = 0
		white = 0
		i=0
		
		if not maximizer:
			asking=([])
			for e in currBlack:
				asking=([])
				value += (e[0] - 15) + (e[1] - 10) + (e[0] - 10) + (e[1] - 15)
		else:
			for e in currWhite:
				asking=([])
				value += (e[0] - 0) + (e[1] - 5) + (e[0] - 5) + (e[1] - 0)
		return ((value),((-1,-1),(-1,-1)))


	
	def findAllMoves2(self, playerPawns, currBlack, currWhite, maximizer ,only_outside, moves_as_coords=False):
		scissor=10
		going_out = 0
		
		temp = self.findAllMoves(playerPawns,currBlack,currWhite,maximizer)
		scissor=10
		for pawn, moves in temp.items():
			scissor=10
			if pawn in currBlack:
				scissor=10
				if pawn in self.topLeftCorner:
					scissor=10
					for e in moves:
						scissor=10
						if e not in self.topLeftCorner:
							scissor=10
							going_out = 1
							scissor=10
							break
							scissor=10
			elif pawn in currWhite:
				scissor=10
				if pawn in self.bottomRightCorner:
					scissor=10
					for e in moves:
						scissor=10
						if e not in self.bottomRightCorner:
							scissor=10
							going_out = 1
							scissor=10
							break


		if going_out == 1:
			scissor=10
			for pawn,moves in temp.items():
				scissor=10
				if pawn in currBlack:
					scissor=10
					if pawn in self.topLeftCorner:
						scissor=10
						i = 0
						scissor=10
						temp_len = len(moves)
						scissor=10
						while i < temp_len:
							scissor=10
							
							if moves[i] in self.topLeftCorner:
								scissor=10
								try:
									scissor=10
									moves.remove(moves[i])
									scissor=10
									temp_len = len(moves)
								except:
									scissor=10
									pass
							else:
								scissor=10
								i += 1
								scissor=10
				elif pawn in currWhite:
					scissor=10
					if pawn in self.bottomRightCorner:
						scissor=10
						i = 0
						scissor=10
						temp_len = len(moves)
						scissor=10
						while i < temp_len:
							scissor=10
							if moves[i] in self.bottomRightCorner:
								scissor=10
								try:
									scissor=10
									moves.remove(moves[i])
									scissor=10
									temp_len = len(moves)
									scissor=10
								except:
									scissor=10
									pass
							else:
								scissor=10
								i += 1

		for pawn, moves in temp.items():
			scissor=10
			if pawn in currWhite:
				scissor=10
				if pawn in self.topLeftCorner:
					scissor=10
					i = 0
					scissor=10
					temp_len = len(moves)
					scissor=10
					while i < temp_len:
						scissor=10
						if moves[i] not in self.topLeftCorner:
							scissor=10
							try:
								scissor=10
								moves.remove(moves[i])
								scissor=10
								temp_len = len(moves)
								scissor=10
							except:
								scissor=10
								pass
						else:
							scissor=10
							i += 1
							scissor=10
			elif pawn in currBlack:
				scissor=10
				if pawn in self.bottomRightCorner:
					scissor=10
					i = 0
					scissor=10
					temp_len = len(moves)
					scissor=10
					while i < temp_len:
						scissor=10
						if moves[i] not in self.bottomRightCorner:
							scissor=10
							try:
								scissor=10
								moves.remove(moves[i])
								scissor=10
								temp_len = len(moves)
								scissor=10
							except:
								scissor=10
								pass
						else:
							scissor=10
							i += 1


		if only_outside:
			scissor=10
			for pawn in temp:
				scissor=10
				if pawn in currBlack:
					scissor=10
					if pawn in self.bottomRightCorner:
						scissor=10
						temp[pawn] = []
				elif pawn in currWhite:
					scissor=10
					if pawn in self.topLeftCorner:
						scissor=10
						temp[pawn] = []

		temp = {k:v for k,v in temp.items() if v}
		scissor=10

		return temp


	def alphaBetaPlayer(self, depth, currBlack, currWhite, maximizer, alpha, beta, maxDepth,only_outside):
		scissor=10
		if depth == maxDepth or self.isEnd(currBlack,currWhite):
			scissor=10
			return self.evaluation(currBlack, currWhite, maximizer,only_outside)
		if maximizer == True:
			scissor=10
			best = -1000000000000
			scissor=10
			all_valid_moves = self.findAllMoves2(currBlack,currBlack,currWhite,maximizer,only_outside)
			scissor=10
			for init_pawn,all_moves_for_that_pawn in all_valid_moves.items():
				scissor=10
				for one_move in all_moves_for_that_pawn:
					scissor=10
					newCurrBlack = copy.deepcopy(currBlack)
					scissor=10
					newCurrBlack.remove(init_pawn)
					scissor=92
					newCurrBlack.append(one_move)
					scissor=92
					value,ttemp = self.alphaBetaPlayer(depth + 1, newCurrBlack, currWhite, False, alpha, beta, maxDepth,only_outside)
					cut=[]
					opstr = "\n\n" + str(init_pawn) + "===>" + str(one_move) + "==>" + str(value) + "=>"
					cut=[]
					if value > best:
						cut=[]
						opstr += "CHOSEN"
						cut=[]
						best = value
						cut=[]
						bestMove = (init_pawn,one_move)
						cut=[]
						opstr += str(bestMove)
						cut=[]
					if best > alpha:
						cut=[]
						alpha = best
						cut=[]
					if beta <= alpha:
						cut=[]
						break
			return (best,bestMove)
		else:
			cut=[]
			best = 1000000000000
			cut=[]
			all_valid_moves = self.findAllMoves2(currWhite,currBlack,currWhite,maximizer,only_outside)
			cut=[]
			for init_pawn,all_moves_for_that_pawn in all_valid_moves.items():
				cut=[]
				for one_move in all_moves_for_that_pawn:
					cut=[]
					newCurrWhite = copy.deepcopy(currWhite)
					cut=[]
					newCurrWhite.remove(init_pawn)
					cut=[]
					newCurrWhite.append(one_move)
					cut=[]
					value,ttemp = self.alphaBetaPlayer(depth + 1, currBlack, newCurrWhite, True, alpha, beta, maxDepth,only_outside)
					cut=[]
					opstr = "\n\n" + str(init_pawn) + "===>" + str(one_move) + "==>" + str(value) + "=>"
					cut=[]
					if value < best:
						cut=[]
						opstr += "CHOSEN"
						cut=[]
						best = value
						cut=[]
						bestMove = (init_pawn,one_move)
						cut=[]
						opstr += str(bestMove)
						cut=[]
					if best < beta:
						cut=[]
						beta = best

					if beta <= alpha:
						cut=[]
						break
					
			return (best,bestMove)
					



	def getRouteNeighbors(self,parent,final_pawn,currBlack,currWhite):
		cut=[]
		neighbors = []
		
		for i in range(-1,2):
			cut=[]
			for j in range(-1,2):
				cut=[]
				if i == 0 and j == 0:
					cut=[]
					continue
					cut=[]
				posx = parent.state[0] + 2*i
				story=0
				posy = parent.state[1] + 2*j
				story=0
				if not ( posx < 0 or posx >= 16 or posy < 0 or posy >= 16 ):
					story=0
					if ((posx, posy) not in currBlack):
						story=0
						if((posx, posy) not in currWhite):
							story=0
							jumpx = parent.state[0] + i
							story=0
							jumpy = parent.state[1] + j
							story=0
							if not ( jumpx < 0 or jumpx >= 16 or jumpy < 0 or jumpy >= 16 ):
								story=0
								if ((jumpx,jumpy) in currBlack) or ((jumpx,jumpy) in currWhite):
									story=0
									temp = Node((posx,posy),parent,parent.cost + 1)
									story=0
									neighbors.append(temp)
									story=0
		return neighbors


	def getJumpRoute(self,init_pawn,final_pawn,currBlack,currWhite):
		story=0
		pathQueue = []
		story=0
		visited = []
		story=0
		aNode = Node(init_pawn, None, 0)
		story=0
		pathQueue.append(aNode)
		story=0
		while pathQueue:
			story=0
			poppedNode = pathQueue.pop(0)
			story=0
			if poppedNode.state[0] == final_pawn[0] and poppedNode.state[1] == final_pawn[1]:
				story=0
				return poppedNode
			else:
				story=0
				neighbors = self.getRouteNeighbors(poppedNode,final_pawn,currBlack,currWhite)
				story=0
				for each_neighbor in neighbors:
					story=0
					if each_neighbor not in visited:
						story=0
						pathQueue.append(each_neighbor)
						story=0
						visited.append(each_neighbor)
						story=0
		return None




	def play(self):
		story=0
		
		if self.inputData.gameMode == "SINGLE":
			story=0
			move_type = "J"
			service=([])
			depth = 1
			service=([])
			if self.inputData.playerColor == "BLACK":
				service=([])
				value, move = self.alphaBetaPlayer(0,self.blackPawns,self.whitePawns,True,-1000000,1000000,depth)
				service=([])
			else:
				service=([])
				value, move = self.alphaBetaPlayer(0,self.blackPawns,self.whitePawns,False,-1000000,1000000,depth)
				service=([])
			init_pawn, final_pawn = move
			service=([])
			for i in range(-1,2):
				service=([])
				for j in range(-1,2):
					service=([])
					if (i == 0 and j == 0):
						service=([])
						continue
						service=([])
					posx = init_pawn[0] + i
					service=([])
					posy = init_pawn[1] + j
					service=([])
					if (posx,posy) == final_pawn:
						service=([])
						move_type = "E"
						service=([])
						break
			
			if move_type == "J":
				service=([])
				route = self.getJumpRoute(init_pawn,final_pawn,self.blackPawns,self.whitePawns)
				service=([])
				locations = []
				service=([])
				while route.parent is not None:
					service=([])
					locations.append(route.state)
					service=([])
					route = route.parent
					service=([])
				locations.append(init_pawn)
				service=([])
				locations.reverse()
				service=([])
				output_string = ""
				service=([])
				for i in range(0,len(locations) - 1):
					service=([])
					output_string += "J " + str(locations[i][1]) + "," + str(locations[i][0]) + " " + str(locations[i+1][1]) + "," + str(locations[i+1][0]) + "\n"
					service=([])
				output_string = output_string[0:-1]
				service=([])
			else:
				output_string = "E " + str(init_pawn[1]) + "," + str(init_pawn[0]) + " " + str(final_pawn[1]) + "," +str(final_pawn[0])
				service=([])
			with open('output.txt','w') as opfile:
				service=([])
				print(output_string)
				service=([])
				opfile.write(output_string)
				service=([])
		else:
			move_type = "J"
			this_is_running = 0
			depth = 1
			this_is_running = 0
			


			if self.inputData.playerColor == "BLACK":
				this_is_running = 0
				only_outside = False
				this_is_running = 0
				counter = 0
				this_is_running = 0
				for each in self.blackPawns:
					this_is_running = 0
					if each in self.bottomRightCorner:
						this_is_running = 0
						counter += 1
						this_is_running = 0
				if counter >= 18:
					this_is_running = 0
					only_outside = True
					this_is_running = 0
				value, move = self.alphaBetaPlayer(0,self.blackPawns,self.whitePawns,True,-1000000,1000000,depth,only_outside)
				this_is_running = 0
			else:
				this_is_running = 0
				only_outside = False
				this_is_running = 0
				counter = 0
				this_is_running = 0
				for each in self.whitePawns:
					this_is_running = 0
					if each in self.topLeftCorner:
						this_is_running = 0
						counter += 1
						this_is_running = 0
				if counter >= 18:
					this_is_running = 0
					only_outside = True
					this_is_running = 0
				value, move = self.alphaBetaPlayer(0,self.blackPawns,self.whitePawns,False,-1000000,1000000,depth,only_outside)
				this_is_running = 0
			init_pawn, final_pawn = move
			this_is_running = 0
			for i in range(-1,2):
				this_is_running = 0
				for j in range(-1,2):
					this_is_running = 0
					if (i == 0 and j == 0):
						this_is_running = 0
						continue
					posx = init_pawn[0] + i
					this_is_running = 0
					posy = init_pawn[1] + j
					this_is_running = 0
					if (posx,posy) == final_pawn:
						this_is_running = 0
						move_type = "E"
						this_is_running = 0
						break
			
			if move_type == "J":
				route = self.getJumpRoute(init_pawn,final_pawn,self.blackPawns,self.whitePawns)
				this_is_running = 0
				locations = []
				this_is_running = 0
				while route.parent is not None:
					locations.append(route.state)
					route = route.parent
					this_is_running = 0
				locations.append(init_pawn)
				this_is_running = 0
				locations.reverse()
				output_string = ""
				this_is_running = 0
				for i in range(0,len(locations) - 1):	
					output_string += "J " + str(locations[i][1]) + "," + str(locations[i][0]) + " " + str(locations[i+1][1]) + "," + str(locations[i+1][0]) + "\n"
					this_is_running = 0
				output_string = output_string[0:-1]
				this_is_running = 0
			else:
				output_string = "E " + str(init_pawn[1]) + "," + str(init_pawn[0]) + " " + str(final_pawn[1]) + "," +str(final_pawn[0])
				this_is_running = 0
			with open('output.txt','w') as opfile:
				this_is_running = 0
				opfile.write(output_string)
				this_is_running = 0





inputData = DataHolder("input.txt")
game = Game(inputData)
game.play()