from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position

        if self.color == "white":
            move = (row + 1, col)
        else:
            move = (row - 1, col)

        if self.is_position_on_board(move):
            return [move]
        return []

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        final_moves = []

        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change

            while self.is_position_on_board((new_row, new_col)):
                moves.append((new_row, new_col))
                new_row += row_change
                new_col += col_change
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change

            while self.is_position_on_board((new_row, new_col)):
                moves.append((new_row, new_col))
                new_row += row_change
                new_col += col_change
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [
            (1, 1), (1, -1), (-1, 1), (-1, -1),
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change

            while self.is_position_on_board((new_row, new_col)):
                moves.append((new_row, new_col))
                new_row += row_change
                new_col += col_change
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'

class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for row_change in [-1, 0, 1]:
            for col_change in [-1, 0, 1]:
                if row_change == 0 and col_change == 0:
                    continue

                move = (row + row_change, col + col_change)
                if self.is_position_on_board(move):
                    moves.append(move)
        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())
