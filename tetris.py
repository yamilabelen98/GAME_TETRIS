import pygame
import random

# Configuraciones básicas
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
BOARD_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
BOARD_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Inicializa pygame
pygame.init()

# Inicializar el mixer para manejar el sonido
pygame.mixer.init()

# Cargar la música del juego
pygame.mixer.music.load("tetris_music.mp3.mp3")
pygame.mixer.music.play(-1)  # Reproduce la música en bucle infinito (-1)
pygame.mixer.music.set_volume(0.5)  # Establecer volumen inicial en 50%

# Crear la ventana del juego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# Inicializar el reloj para controlar los FPS
clock = pygame.time.Clock()

# Fuente para el texto de "Game Over"
font = pygame.font.SysFont('Arial', 36)

# Piezas de Tetris
PIECES = [
    [[1, 1], [1, 1]],  # Cuadrado
    [[1, 1, 1, 1]],    # Línea
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]]   # S
]

# Funciones del juego
def create_board():
    return [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

def draw_board(board):
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            if value:
                pygame.draw.rect(screen, YELLOW, pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_piece(piece, position):
    for y, row in enumerate(piece):
        for x, value in enumerate(row):
            if value:
                pygame.draw.rect(screen, RED, pygame.Rect((position['x'] + x) * BLOCK_SIZE, (position['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Pantalla "Game Over"
def draw_game_over():
    screen.fill(BLACK)
    game_over_text = font.render("Game Over", True, RED)
    restart_text = font.render("Press Enter to Restart", True, YELLOW)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + game_over_text.get_height()))
    pygame.display.update()

def check_collision(board, piece, offset):
    for y, row in enumerate(piece):
        for x, value in enumerate(row):
            if value:
                if (y + offset['y'] >= len(board) or 
                    x + offset['x'] < 0 or 
                    x + offset['x'] >= len(board[0]) or 
                    board[y + offset['y']][x + offset['x']]):
                    return True
    return False

def solidify_piece(board, piece, offset):
    for y, row in enumerate(piece):
        for x, value in enumerate(row):
            if value:
                board[y + offset['y']][x + offset['x']] = 1

def remove_rows(board):
    new_board = [row for row in board if not all(row)]
    rows_removed = len(board) - len(new_board)
    board[:] = [[0] * BOARD_WIDTH for _ in range(rows_removed)] + new_board

def rotate_piece(piece):
    return [list(row) for row in zip(*piece[::-1])]

def game_loop():
    # Crear el tablero y la primera pieza
    board = create_board()
    piece = random.choice(PIECES)
    piece_position = {'x': BOARD_WIDTH // 2 - len(piece[0]) // 2, 'y': 0}

    # Variables del juego
    running = True
    paused = False  # Variable para controlar la pausa
    drop_counter = 0
    drop_speed = 500  # Velocidad de caída en milisegundos
    volume = 0.5  # Volumen inicial
    game_over = False  # Variable para indicar si el juego ha terminado

    while running:
        screen.fill(BLACK)
        draw_board(board)
        draw_piece(piece, piece_position)

        pygame.display.update()
        drop_counter += clock.get_rawtime()
        clock.tick()

        if not paused and not game_over:  # Solo hacer que las piezas caigan si no está en pausa o en "Game Over"
            if drop_counter > drop_speed:
                piece_position['y'] += 1
                drop_counter = 0
                if check_collision(board, piece, piece_position):
                    piece_position['y'] -= 1
                    solidify_piece(board, piece, piece_position)
                    remove_rows(board)
                    piece = random.choice(PIECES)
                    piece_position = {'x': BOARD_WIDTH // 2 - len(piece[0]) // 2, 'y': 0}
                    if check_collision(board, piece, piece_position):
                        game_over = True  # "Game Over"

        # Manejo de eventos de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not paused and not game_over:
                    piece_position['x'] -= 1
                    if check_collision(board, piece, piece_position):
                        piece_position['x'] += 1
                if event.key == pygame.K_RIGHT and not paused and not game_over:
                    piece_position['x'] += 1
                    if check_collision(board, piece, piece_position):
                        piece_position['x'] -= 1
                if event.key == pygame.K_DOWN and not paused and not game_over:
                    piece_position['y'] += 1
                    if check_collision(board, piece, piece_position):
                        piece_position['y'] -= 1
                        solidify_piece(board, piece, piece_position)
                        remove_rows(board)
                        piece = random.choice(PIECES)
                        piece_position = {'x': BOARD_WIDTH // 2 - len(piece[0]) // 2, 'y': 0}
                if event.key == pygame.K_UP and not paused and not game_over:
                    rotated_piece = rotate_piece(piece)
                    if not check_collision(board, rotated_piece, piece_position):
                        piece = rotated_piece

                # Pausar/continuar el juego con la tecla "Enter"
                if event.key == pygame.K_RETURN:
                    paused = not paused
                    if paused:
                        pygame.mixer.music.pause()  # Pausar la música
                    else:
                        pygame.mixer.music.unpause()  # Reanudar la música

                # Subir volumen 
                if event.key == pygame.K_F3:
                    volume = min(1.0, volume + 0.1)  # Máximo volumen es 1.0
                    pygame.mixer.music.set_volume(volume)
                    print(f"Volumen: {volume * 100:.0f}%")

                # Bajar volumen
                if event.key == pygame.K_F2:
                    volume = max(0.0, volume - 0.1)  # Mínimo volumen es 0.0
                    pygame.mixer.music.set_volume(volume)
                    print(f"Volumen: {volume * 100:.0f}%")

        if game_over:
            draw_game_over()  # Mostrar la pantalla de "Game Over"
            while True:  # Esperar hasta que el jugador elija qué hacer
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:  # Presionar "Enter"
                            return True  # Reinicia el juego
                        if event.key == pygame.K_ESCAPE:  # Presionar "Esc" para salir
                            running = False
                            break
                if not running:
                    break

if __name__ == "__main__":
    while True:
        if not game_loop():
            break
    pygame.quit()
