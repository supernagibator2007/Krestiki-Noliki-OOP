from gameparts import Board
import pygame


pygame.init()

CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)


def save_result(winner):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(winner + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_column = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_column] == ' ':
                    game.board[clicked_row][clicked_column] = current_player
                    draw_figures(game.board)

                if game.find_winner(current_player):
                    winner = f'Победил {current_player}'
                    print(winner)
                    save_result(winner)
                    running = False
                elif game.is_board_full():
                    result = 'Ничья'
                    print(result)
                    save_result(result)
                    running = False

                current_player = 'O' if current_player == 'X' else 'X'

        pygame.display.update()

    pygame.quit()


def draw_line():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )


def draw_figures(board):
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if board[row][column] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        column * CELL_SIZE + SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    (
                        column * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        column * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        column * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][column] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        column * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


if __name__ == '__main__':
    draw_line()
    main()
