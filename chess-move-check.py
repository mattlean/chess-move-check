import sys

### Constants ###
BOARD_SIZE = 8
COLORSET = set(['black', 'white']) # Used for checking if input color is valid


### Utility Functions ###
# Validates attribute with set. Returns normalized attribute on success.
def validAttr(attr, checkSet):
	normalAttr = attr.lower()

	if normalAttr in checkSet:
		return normalAttr

	raise Exception('You input an invalid color or piece name!')

# Converts input position from chess format (ex. B:3) to list index format (ex. 1,2)
def formatIndex(position):
	splitPos = position.split(':')
	charCoord = splitPos[0].capitalize()

	if charCoord not in Piece._CHARMAP:
		raise Exception('You input a piece with an invalid X coordinate!')

	if int(splitPos[1]) < 1 or int(splitPos[1]) > BOARD_SIZE:
		raise Exception('You input a piece with an invalid Y coordinate!')

	return {'x': Piece._CHARMAP[charCoord], 'y': int(splitPos[1]) - 1}

# Converts input position from list index format (ex. 1,2) to chess format (ex. B:3)
def formatChess(position):
	return {'x': Piece._INDEXMAP[position['x']], 'y': str(position['y'] + 1)}


### Parent class for all piece types ###
class Piece:
	# Used for converting from chess to index format
	_CHARMAP = {
		'A': 0,
		'B': 1,
		'C': 2,
		'D': 3,
		'E': 4,
		'F': 5,
		'G': 6,
		'H': 7
	}

	# Used for converting from index to chess format
	_INDEXMAP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

	# Used for checking if input piece name is valid
	_NAMESET = set(['bishop', 'king', 'knight', 'pawn', 'queen', 'rook'])

	# Constructor
	def __init__(self, color, name, position):
		self.color = validAttr(color, COLORSET)
		self.name = validAttr(name, Piece._NAMESET)
		self.position = formatIndex(position)

	# Implementation for move validation. Changes depending on piece type.
	def _moveCalc(self, board):
		raise NotImplementedError

	# Checks for possible moves for piece. Returns list of possible moves.
	def moveCheck(self, board):
		return self.moveCalc(board)

	# Prints out piece info (Color, Name, Position)
	def printPiece(self):
		print self.color.capitalize() + ', ' + self.name.capitalize() + ', <' + str(self.position['x']) + ':' + str(self.position['y']) + '>'


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

		# Populate pieces
		for i in range(len(pieces)):
			splitData = pieces[i].split(',')

			if len(splitData) < 3:
				raise Exception('You input an invalid piece!')

			newPiece = Piece(splitData[0], splitData[1], splitData[2])
			self.board[newPiece.position['x']][newPiece.position['y']] = newPiece
			self.pieces.append(newPiece)

	# Show what is at position (x,y)
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
### File I/O ###
inputFile = open(sys.argv[1])
fileBreakdown = inputFile.read().splitlines()
inputFile.close()

chessboard = Chessboard(validAttr(fileBreakdown[0], COLORSET), fileBreakdown[1:])
chessboard.printData()
#chessboard.printPos(0,3)
chessboard.printPos(7,7)

"""piece = Piece('bLaCk', 'KiNg', 'H:8')
piece.printPiece()
chessPos = formatChess(piece.position)
print '<' + chessPos['x'] + ':' + chessPos['y'] + '>'

print sys.argv"""
