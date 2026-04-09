# Tic Tac Toe GUI - Versión Gráfica
# Tech stack: Python 3.x, pygame
# Domain: GUI Juego
# Description: Versión gráfica del Tic Tac Toe con menú y tablero interactivo.
# Style: Programación orientada a objetos, prácticas modernas de Python 2026.

import pygame
import sys

# Constantes
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colores
BG_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (80, 80, 80)
BUTTON_HOVER = (130, 130, 130)

# Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe GUI")
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 30)

# Estados del juego
MENU = 'menu'
GAME = 'game'
state = MENU

# Función para dibujar texto centrado
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Función para dibujar botón
def draw_button(text, x, y, width, height, color, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    draw_text(text, small_font, TEXT_COLOR, x + width // 2, y + height // 2)
    return False

# Función para dibujar menú
def draw_menu():
    screen.fill(BG_COLOR)
    draw_text("Tic Tac Toe", font, TEXT_COLOR, WIDTH // 2, 100)

    if draw_button("Iniciar Juego", 200, 200, 200, 50, BUTTON_COLOR, BUTTON_HOVER):
        global state, board, player, game_over
        state = GAME
        board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        player = 'X'
        game_over = False

    if draw_button("Salir", 200, 300, 200, 50, BUTTON_COLOR, BUTTON_HOVER):
        pygame.quit()
        sys.exit()

# Función para dibujar líneas del tablero
def draw_lines():
    # Líneas horizontales
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Líneas verticales
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Función para dibujar figuras (X o O)
def draw_figures(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Función para marcar cuadrado
def mark_square(row, col, player):
    board[row][col] = player

# Función para verificar cuadrado disponible
def available_square(row, col):
    return board[row][col] == ' '

# Función para verificar si tablero está lleno
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == ' ':
                return False
    return True

# Función para verificar victoria
def check_win(player):
    # Verificar filas
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # Verificar columnas
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Función para dibujar estado del juego
def draw_game_status():
    if game_over:
        if check_win('X'):
            draw_text("¡X Gana!", font, TEXT_COLOR, WIDTH // 2, HEIGHT // 2 - 50)
        elif check_win('O'):
            draw_text("¡O Gana!", font, TEXT_COLOR, WIDTH // 2, HEIGHT // 2 - 50)
        else:
            draw_text("¡Empate!", font, TEXT_COLOR, WIDTH // 2, HEIGHT // 2 - 50)
        if draw_button("Jugar de Nuevo", 200, HEIGHT // 2 + 50, 200, 50, BUTTON_COLOR, BUTTON_HOVER):
            global state
            state = MENU

# Inicializar variables
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 'X'
game_over = False

# Loop principal
while True:
    if state == MENU:
        draw_menu()
    elif state == GAME:
        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures(board)
        draw_game_status()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if state == GAME and event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                elif is_board_full():
                    game_over = True
                player = 'O' if player == 'X' else 'X'

    pygame.display.update()