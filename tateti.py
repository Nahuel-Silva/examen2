class TaTeTi():

    def __init__(self, piece=""):
        self.board = {"1.1": "1.1", "1.2": "1.2", "1.3": "1.3",
                      "2.1": "2.1", "2.2": "2.2", "2.3": "2.3",
                      "3.1": "3.1", "3.2": "3.2", "3.3": "3.3"}

        self.valid = ["1.1", "1.2", "1.3",
                      "2.1", "2.2", "2.3",
                      "3.1", "3.2", "3.3"]

        self.piece = piece

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        self._piece = piece

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, valid):
        self._valid = valid

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    def __str__(self):
        exp = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n'
        exp += '---+---+---\n3.1|3.2|3.3'
        return exp

    def win(self):
        board = self.board
        for n in board:
            if (board['1.1'] == ' x ' and
                    board['2.2'] == ' x ' and
                    board['3.3'] == ' x '):
                return True
            if (board['1.1'] == ' x ' and
                    board['2.1'] == ' x ' and
                    board['3.1'] == ' x '):
                return True
            if (board['1.2'] == ' o ' and
                    board['2.2'] == ' o ' and
                    board['3.2'] == ' o '):
                return True
            if (board['3.1'] == ' x ' and
                    board['2.2'] == ' x ' and
                    board['1.3'] == ' x '):
                return True
            if (board['1.1'] == ' o ' and
                    board['1.2'] == ' o ' and
                    board['1.3'] == ' o '):
                return True
            if (board['2.1'] == ' x ' and
                    board['2.2'] == ' x ' and
                    board['2.3'] == ' x '):
                return True
            else:
                return False

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner

    def input_position(self):
        while True:
            val = str(input("Ingrese la posicion: "))
            if val in self.valid:
                self.valid.remove(val)
                return val
            else:
                print("error posicion no valida")


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
