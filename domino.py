# 6 4 2 3 4 8 1 1 7 4 7 2 8 (ok)
# 6 1 4 2 3 4 1 7 4 7 2 8 1 (sem combinacoes)
# 11 2 2 10 9 3 10 4 2 3 4 8 1 1 7 4 7 2 8 3 3 2 2 (ok)
# 10 2 2 10 9 3 10 4 2 3 4 8 1 1 7 4 7 2 8 3 3 (ok)
# 18 6 2 5 5 6 7 7 0 5 2 10 7 8 1 10 9 9 6 6 4 5 10 9 2 8 6 8 8 8 2 9 5 0 4 1 2 (sem combinacoes)

import sys


def match_pieces(p1, p2):
	return p1[1] == p2[0]


def flip_piece(p):
	result = (p[1], p[0])
	return result


class Domino:
	def __init__(self, pieces, number_of_pieces, DEBUG=False):
		self.pieces = pieces
		self.number_of_pieces = number_of_pieces
		self.chain = list()
		self.DEBUG = DEBUG
	
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
	
	def report(self):
		if self.DEBUG:
			print(5*"+==+" + "REPORT" + 5*"+==+")
			self.print_pieces()
			self.print_chain()
			print(10 * "+==+")
	
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
		self.report()
		possibles_pieces = list()
		if len(self.chain) == 0:
			has_pieces, possibles_pieces = self.possibles_pieces(tuple())
			if not has_pieces: raise ValueError("Should not be false")
		else:
			has_pieces, possibles_pieces = self.possibles_pieces(self.chain[len(self.chain)-1])  # possiveis pecas para a ultima posicao
			if not has_pieces:
				if len(self.pieces) > 0: # Cheguei num beco sem saida
					return False
				else:
					return True
		
		for p in possibles_pieces:
			self.chain.append(p)
			
			if p in self.pieces:
				self.pieces.remove(p)
			elif flip_piece(p) in self.pieces:
				self.pieces.remove(flip_piece(p))
			else:
				raise ValueError("Piece could not be removed")
			
			result = self.solve()
			if result:
				if self.DEBUG: print("breaking...")
				return True
			else:
				p = self.chain.pop()
				self.pieces.append(p)
				if self.DEBUG: print(f'no pieces available for {p}')
		
		return False


number_of_pieces = int(sys.argv[1])
pieces = list()

for i in range(number_of_pieces):
	pieces.append((int(sys.argv[2 * i + 2]), int(sys.argv[2 * i + 3])))

d = Domino(pieces, number_of_pieces)

result = d.solve()
if result:
	d.print_chain()
else:
	print("Sem combinações possíveis")
	
#print(f'#### Result => {result}')
#d.print_pieces()
