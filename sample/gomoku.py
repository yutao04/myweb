import pygame
import sys
import tkinter as tk
from tkinter import messagebox
import random

# グローバル変数
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
CELL_SIZE = WIDTH // 20

# 画面の初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("五目並べ")
# 緑で塗りつぶす
screen.fill((0, 128, 0))
# 盤面の線を描画
for i in range(1, 20):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

# オセロの駒の色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def check_win(board, player):
    # 横のチェック
    for row in board:
        for i in range(len(row) - 4):  # 5つの駒が並ぶ可能性がある範囲までループ
            if all(cell == player for cell in row[i:i+5]):
                return True
    # 縦のチェック
    for col in range(len(board[0])):
        for i in range(len(board) - 4):  # 5つの駒が並ぶ可能性がある範囲までループ
            if all(board[row][col] == player for row in range(i, i+5)):
                return True
    # 斜めのチェック（左上から右下）
    for row in range(len(board) - 4):  # 左上から右下にかけての斜めのラインをチェック
        for col in range(len(board[0]) - 4):
            if all(board[row+i][col+i] == player for i in range(5)):
                return True
    # 斜めのチェック（右上から左下）
    for row in range(len(board) - 4):  # 右上から左下にかけての斜めのラインをチェック
        for col in range(len(board[0]) - 1, 3, -1):
            if all(board[row+i][col-i] == player for i in range(5)):
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
                    if board[row][col] == 'X':
                            n = random.randint(0,99)
                            if n < 80:
                                pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
                            else :
                                pygame.draw.circle(screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
                    elif board[row][col] == 'O':
                            n = random.randint(0,99)
                            if n < 80:
                                pygame.draw.circle(screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
                            else :
                                pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
                    if 0 <= row < 20 and 0 <= col < 20 and board[row][col] == " ":
                        player = players[turn % 2]
                        board[row][col] = player
                        if check_win(board, player):
                            messagebox.showinfo("勝敗",f"プレイヤー{player}の勝利!" )
                            print(f"Player {player} の勝利です！")
                            running = False
                        elif is_full(board):
                            messagebox.showinfo("勝敗",f"引き分け")
                            print("引き分けです！")
                            running = False
                        else:
                            turn += 1

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
