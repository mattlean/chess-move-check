import sys

### Constants ###
BOARD_SIZE = 8
# Used for converting from chess to index format
CHARMAP = {
	'A': 0,
	'B': 1,
	'C': 2,
	'D': 3,
	'E': 4,
	'F': 5,
	'G': 6,
	'H': 7
}
COLORSET = set(['Black', 'White']) # Used for checking if input color is valid
INDEXARR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # Used for converting from index to chess format
NAMEARR = ['Bishop', 'King', 'Knight', 'Pawn', 'Queen', 'Rook'] # Used for checking the appropriate piece name

### Utility Functions ###
# Validates attribute with set. Returns normalized attribute on success.
def validAttr(attr, checkSet):
	normalAttr = attr.lower().capitalize()

	if normalAttr in checkSet:
		return normalAttr

	raise Exception('You input an invalid color or piece name!')

# Converts input position from chess format (ex. B:3) to list index format (ex. 1,2)
def formatIndex(position):
	splitPos = position.split(':')
	charCoord = splitPos[0].capitalize()

	if charCoord not in CHARMAP:
		raise Exception('You input a piece with an invalid X coordinate!')

	if int(splitPos[1]) < 1 or int(splitPos[1]) > BOARD_SIZE:
		raise Exception('You input a piece with an invalid Y coordinate!')

	return {'x': CHARMAP[charCoord], 'y': int(splitPos[1]) - 1}

# Converts input position from list index format (ex. 1,2) to chess format (ex. B:3)
def formatChess(position):
	return '<' + INDEXARR[position['x']] + ':' + str(position['y'] + 1) + '>'


### Parent class for all piece types ###
class Piece:
	# Constructor
	def __init__(self, color, name, position):
		self.color = validAttr(color, COLORSET)
		self.name = validAttr(name, NAMEARR)
		self.position = formatIndex(position)

	# Checks if input position (must be in index format) is within the bounds of the board
	def checkBounds(self, x, y):
		if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
			return False
		return True

	# Implementation for move validation. Changes depending on piece type.
	def calcMoves(self, board):
		raise NotImplementedError

	# Prints out piece info (Color, Name, Position)
	def printPiece(self):
		position = formatChess(self.position)
		print self.color.capitalize() + ', ' + self.name.capitalize() + ', ' + position


### King Class which inherits from Piece ###
class King(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		possibleMoves = [] # List of possible moves to return

		# Makes code below easier to read
		x = self.position['x']
		y = self.position['y']

		# Move up
		if self.checkBounds(x, y + 1):
			possibleMoves.append({'x': x, 'y': y + 1})
		
		# Move up-right
		if self.checkBounds(x + 1, y + 1):
			possibleMoves.append({'x': x + 1, 'y': y + 1})

		# Move right
		if self.checkBounds(x + 1, y):
			possibleMoves.append({'x': x + 1, 'y': y})

		# Move down-right
		if self.checkBounds(x + 1, y - 1):
			possibleMoves.append({'x': x + 1, 'y': y - 1})

		# Move down
		if self.checkBounds(x, y - 1):
			possibleMoves.append({'x': x, 'y': y - 1})

		# Move down-left
		if self.checkBounds(x - 1, y - 1):
			possibleMoves.append({'x': x - 1, 'y': y - 1})

		# Move left
		if self.checkBounds(x - 1, y):
			possibleMoves.append({'x': x - 1, 'y': y})

		# Move up-left
		if self.checkBounds(x - 1, y + 1):
			possibleMoves.append({'x': x - 1, 'y': y + 1})

		return possibleMoves


### Pawn Class which inherits from Piece ###
class Pawn(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Rook Class which inherits from Piece ###
class Rook(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Bishop Class which inherits from Piece ###
class Bishop(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Queen Class which inherits from Piece ###
class Queen(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Knight Class which inherits from Piece ###
class Knight(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Chessboard Class ###
class Chessboard:
	def __init__(self, playerColor, pieces):
		self.playerColor = playerColor # Current player color to determine who's turn it is
		self.pieces = [] # List of all pieces
		self.board = [] # 2D array representation of board

		# Initialize empty board
		for x in range(BOARD_SIZE):
			self.board.append([])
			for y in range(BOARD_SIZE):
				self.board[x].append(None)

		# Populate pieces list
		for i in range(len(pieces)):
			splitData = pieces[i].split(',')

			if len(splitData) < 3:
				raise Exception('You input an invalid piece!')

			# Create the appropriate piece
			if validAttr(splitData[1], NAMEARR) == NAMEARR[0]:
				newPiece = Bishop(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[1]:
				newPiece = King(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[2]:
				newPiece = Knight(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[3]:
				newPiece = Pawn(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[4]:
				newPiece = Queen(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[5]:
				newPiece = Rook(splitData[0], splitData[1], splitData[2])
			
			self.board[newPiece.position['x']][newPiece.position['y']] = newPiece
			self.pieces.append(newPiece)

	def printLegalMoves(self):
		#iterate through each piece and do the following
		currName = chessboard.pieces[0].name
		currPos = chessboard.pieces[0].position
		possibleMoves = chessboard.pieces[0].calcMoves(chessboard.playerColor, chessboard.board)
		
		for possibleMove in possibleMoves:
			print currName + ' at ' + formatChess(currPos) + ' can move to ' + formatChess(possibleMove)

	# Show what is at position (x,y) on the board
	def printPos(self, x, y):
		if self.board[x][y] is None:
			print None
		else:
			self.board[x][y].printPiece()

	# Print chessboard data
	def printData(self):
		print 'Current Player Turn: ' + self.playerColor.capitalize()
		print 'Pieces: ' + str(self.pieces)
		print 'Board: ' + str(self.board)


### main() ###
# File I/O
#print sys.argv
inputFile = open(sys.argv[1])
fileBreakdown = inputFile.read().splitlines()
inputFile.close()

chessboard = Chessboard(validAttr(fileBreakdown[0], COLORSET), fileBreakdown[1:])
chessboard.printLegalMoves()
"""chessboard.printData()
chessboard.printPos(0,3)
chessboard.printPos(7,7)
chessboard.printPos(3,3)
chessboard.printPos(5,2)
chessboard.printPos(5,1)"""
