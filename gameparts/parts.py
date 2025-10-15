class Board:
    """Класс, который описывает игровое поле"""

    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        self.board[row - 1][col - 1] = player

    def display(self):
        print('-' * 5)
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
        print('\n')

    def __str__(self):
        return f'Игровое поле размеров {self.field_size} на {self.field_size}'
