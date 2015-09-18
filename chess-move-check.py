BOARD_SIZE = 8

# Parent class for all piece types
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

	# Used for checking if input color is valid
	_COLORSET = set(['black', 'white'])

	# Used for converting from index to chess format
	_INDEXMAP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

	# Used for checking if input piece name is valid
	_NAMESET = set(['bishop', 'king', 'knight', 'pawn', 'queen', 'rook'])

	# Constructor
	def __init__(self, color, name, position):
		self.color = self._validAttr(color, Piece._COLORSET)
		self.name = self._validAttr(name, Piece._NAMESET)
		self.position = self.indexFormat(position)

	# Validates attribute with set. Returns normalized attribute on success.
	def _validAttr(self, attr, checkSet):
		normalAttr = attr.lower()

		if normalAttr in checkSet:
			return normalAttr

		raise Exception('You input an invalid color or piece name!')

	# Implementation for move validation. Changes depending on piece type.
	def _moveCalc(self, board):
		raise NotImplementedError

	# Checks for possible moves for piece. Returns list of possible moves.
	def moveCheck(self, board):
		return self.moveCalc(board)

	# Converts input position from chess format (ex. B:3) to list index format (ex. 1,2)
	def indexFormat(self, position):
		splitPos = position.split(':')
		charCoord = splitPos[0].capitalize()

		if charCoord not in Piece._CHARMAP:
			raise Exception('You input a piece with an invalid X coordinate!')

		if int(splitPos[1]) < 1 or int(splitPos[1]) > BOARD_SIZE:
			raise Exception('You input a piece with an invalid Y coordinate!')

		return {'x': Piece._CHARMAP[charCoord], 'y': int(splitPos[1]) - 1}

	# Converts input position from list index format (ex. 1,2) to chess format (ex. B:3)
	def chessFormat(self, position):
		return {'x': Piece._INDEXMAP[position['x']], 'y': str(position['y'] + 1)}

	# Prints out piece info (Color, Name, Position)
	def printPiece(self):
		print self.color.capitalize() + ', ' + self.name.capitalize() + ', <' + str(self.position['x']) + ':' + str(self.position['y']) + '>'

class Chessboard:
	def __init__(self, *args):
		# Initialize board
		self.board = []
		self.pieces = []

		for arg in args[1:]:
			print arg

		for x in range(BOARD_SIZE):
			self.board.append([])
			for y in range(BOARD_SIZE):
				self.board[x].append(None)

# main()
chessboard = Chessboard('var', 'meh', 'urmum')

piece = Piece('bLaCk', 'KiNg', 'H:8')
piece.printPiece()

chessPos = piece.chessFormat(piece.position)
print '<' + chessPos['x'] + ':' + chessPos['y'] + '>'
