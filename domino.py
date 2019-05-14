#test 0 6 4 2 3 4 8 1 1 7 4 7 2 8
#test 1 8 1 4 2 3 4 1 7 4 7 2 8

import sys

def match_pieces(p1, p2):
	return p1[1] == p2[0]


def flip_piece(p):
	result = (p[1], p[0])
	return result


class Domino:
	def __init__(self, pieces, number_of_pieces):
		self.pieces = pieces
		self.number_of_pieces = number_of_pieces
		self.chain = list()
		self.count = 0
	
	def print_pieces(self):
		print("Pieces => ", end='')
		for piece in self.pieces:
			print(f'[{piece[0]}|{piece[1]}] ', end='')
		print()
	
	def print_chain(self):
		print("Chain => ", end='')
		for piece in self.chain:
			print(f'[{piece[0]}|{piece[1]}] ', end='')
		print()
	
	def possibles_pieces(self, piece):
		result = list()
		if len(self.pieces) == 0:  # Nao tem nenhuma peca disponivel
			return False, list()
		if not piece:  # Se nao tem nada, todas as pecas estao disponiveis
			return True, self.pieces
		
		for p in self.pieces:
			if match_pieces(piece, p):
				result.append(p)
			elif match_pieces(piece, flip_piece(p)):
				result.append(flip_piece(p))
		return len(result) >= 1, result
	
	def solve(self):
		self.count += 1
		possibles_pieces = list()
		if len(self.chain) == 0:
			has_pieces, possibles_pieces = self.possibles_pieces(tuple())
			if not has_pieces: raise ValueError("Should not be false")
		else:
			has_pieces, possibles_pieces = self.possibles_pieces(self.chain[len(self.chain)-1])  # possiveis pecas para a ultima posicao
			if not has_pieces:
				p = self.chain.pop()
				self.pieces.append(p)
				return False
		
		for p in possibles_pieces:
			self.chain.append(p)
			if p in self.pieces:
				self.pieces.remove(p)
			elif flip_piece(p) in self.pieces:
				self.pieces.remove(flip_piece(p))
			else:
				raise ValueError("Piece could not be removed")
			if self.solve():
				break


number_of_pieces = int(sys.argv[1])
pieces = list()

for i in range(number_of_pieces):
	pieces.append((int(sys.argv[2 * i + 2]), int(sys.argv[2 * i + 3])))

d = Domino(pieces, number_of_pieces)

d.print_pieces()
d.print_chain()

d.solve()
print(f'#### Result')

d.print_pieces()
d.print_chain()
print(d.count)