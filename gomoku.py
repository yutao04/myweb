import pygame
import sys

# グローバル変数
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
CELL_SIZE = WIDTH // 5

# 画面の初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("五目並べ")

# オセロの駒の色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_board(board):
    screen.fill((0, 128, 0))  # 緑で塗りつぶす

    # 盤面の線を描画
    for i in range(1, 5):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

    # マーカーを描画
    for row in range(5):
        for col in range(5):
            if board[row][col] == 'X':
                pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

def check_win(board, player):
    # 横のチェック
    for row in board:
        if all(cell == player for cell in row):
            return True
    # 縦のチェック
    for col in range(5):
        if all(board[row][col] == player for row in range(5)):
            return True
    # 斜めのチェック
    if all(board[i][i] == player for i in range(5)) or all(board[i][4-i] == player for i in range(5)):
        return True
    return False

def is_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def main():
    board = [[" " for _ in range(20)] for _ in range(20)]
    players = ["X", "O"]
    turn = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左クリック
                    x, y = pygame.mouse.get_pos()
                    row = y // CELL_SIZE
                    col = x // CELL_SIZE
                    if 0 <= row < 5 and 0 <= col < 5 and board[row][col] == " ":
                        player = players[turn % 2]
                        board[row][col] = player
                        if check_win(board, player):
                            print(f"Player {player} の勝利です！")
                            running = False
                        elif is_full(board):
                            print("引き分けです！")
                            running = False
                        else:
                            turn += 1

        draw_board(board)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
