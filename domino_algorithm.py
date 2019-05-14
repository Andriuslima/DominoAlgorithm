import sys


def match_pieces(p1, p2):
    return p1[1] == p2[0] or p1[0] == p2[1]


class Domino:
    def __init__(self, pieces):
        self.pieces = pieces
        self.chain = list()

    def print_pieces(self):
        for key, value in self.pieces.items():
            print(f'[{key}] {value}')
    
    def print_chain(self):
        for key in self.chain:
            print("My Chain ==> ", end="")
            print(f'{key}[{self.pieces[key][0]}|{self.pieces[key][1]}] ', end="")
            print('\n')
            print(10*"+=")

    def find_piece(self):
        if len(self.chain) == 0:
            return True, 0
    
        for key, value in self.pieces.items():
            if key not in self.chain and match_pieces(self.pieces[self.chain[len(self.chain)-1]], value):
                return True, key
        return False, None

    def solve(self):
        self.print_chain()
        has_next_piece, next_piece = self.find_piece()
        if not has_next_piece:
            if len(self.chain) == len(self.pieces):
                print("não tem mais o que fazer")
                self.print_chain()
                return
            print("nao tem mais pecas compativeis, voltando")
            self.chain.pop()
            self.solve()
        else:
            print("inserindo na chain")
            self.chain.append(next_piece)
            print(f'Inserido: {self.chain}')
            self.solve()


number_of_pieces = int(sys.argv[1])
pieces = dict()

for i in range(number_of_pieces):
    pieces[i] = (int(sys.argv[2*i + 2]), int(sys.argv[2*i + 3]))

d = Domino(pieces)
d.print_pieces()

print(f'#### Result')

d.solve()
print(d.chain)
