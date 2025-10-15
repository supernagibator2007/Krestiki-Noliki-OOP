from gameparts import Board, FieldIndexError, CellOccupiedError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите x: '))
                if not (0 <= row <= game.field_size):
                    raise FieldIndexError
                column = int(input('Введите y: '))
                if not (0 <= column <= game.field_size):
                    raise FieldIndexError
                if game.board[row - 1][column - 1] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца.')
                continue
            except CellOccupiedError:
                print('Выберите другую ячейку')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
        game.make_move(row, column, current_player)
        game.display()
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
