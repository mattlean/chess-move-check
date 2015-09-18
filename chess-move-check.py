BOARD_SIZE = 8

# Parent class for all piece types
class Piece:
	# Used for converting from chess to index format
	_charMap = {
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
	_indexMap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

	def __init__(self, color, name, position):
		# Initialize and normalize values
		self.color = color.lower().capitalize()
		self.name = name.lower().capitalize()
		self.position = self.indexFormat(position)

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

		if charCoord in Piece._charMap:
			if int(splitPos[1]) < 1 or int(splitPos[1]) > BOARD_SIZE:
				raise Exception('You input a piece with an invalid Y coordinate!')

			return {'x': Piece._charMap[charCoord], 'y': int(splitPos[1]) - 1}
		else:
			raise Exception('You input a piece with an invalid X coordinate!')

	# Converts input position from list index format (ex. 1,2) to chess format (ex. B:3)
	def chessFormat(self, position):
		return {'x': Piece._indexMap[position['x']], 'y': str(position['y'] + 1)}

	def printPiece(self):
		print self.name + ', <' + str(self.position['x']) + ':' + str(self.position['y']) + '>, ' + self.color

class Chessboard:
	def __init__(self):
		# Initialize board
		self.board = []

		for x in range(BOARD_SIZE):
			self.board.append([])
			for y in range(BOARD_SIZE):
				self.board[x].append(None)

# main()
chessboard = Chessboard()

piece = Piece('Black', 'Knight', 'D:8')
piece.printPiece()

chessPos = piece.chessFormat(piece.position)
print '<' + chessPos['x'] + ':' + chessPos['y'] + '>'