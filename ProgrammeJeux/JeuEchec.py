import tkinter as tk
from tkinter import messagebox

# Fenêtre principale
root = tk.Tk()
root.title("Jeu d'échecs")

# Dimensions du plateau
ROWS, COLS = 8, 8
SQUARE_SIZE = 80

# Couleurs du plateau
LIGHT_COLOR = "#F0D9B5"
DARK_COLOR = "#B58863"

# Pièces (unicode)
PIECES = {
    "wr": "♖", "wn": "♘", "wb": "♗", "wq": "♕", "wk": "♔", "wp": "♙",
    "br": "♜", "bn": "♞", "bb": "♝", "bq": "♛", "bk": "♚", "bp": "♟"
}

# Position initiale des pièces (notation simplifiée)
initial_board = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

# Variables globales
current_player = "w"
selected_piece = None
board = initial_board

# Fonction pour dessiner le plateau d'échecs
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
            canvas.create_rectangle(col * SQUARE_SIZE, row * SQUARE_SIZE, (col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, fill=color)

# Fonction pour dessiner les pièces sur le plateau
def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                canvas.create_text(col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2, text=PIECES[piece], font=("Helvetica", 40), tags="piece")

# Fonction pour sélectionner une pièce
def on_square_click(event):
    global selected_piece

    row = event.y // SQUARE_SIZE
    col = event.x // SQUARE_SIZE

    if selected_piece:
        move_piece(selected_piece, (row, col))
        selected_piece = None
    else:
        piece = board[row][col]
        if piece and piece.startswith(current_player):
            selected_piece = (row, col)

# Fonction pour bouger une pièce
def move_piece(start, end):
    global current_player

    start_row, start_col = start
    end_row, end_col = end

    # Vérifier si la case de destination est valide
    piece = board[start_row][start_col]
    target = board[end_row][end_col]

    if target and target[0] == current_player:
        return

    # Déplacer la pièce
    board[end_row][end_col] = piece
    board[start_row][start_col] = ""

    # Dessiner à nouveau le plateau
    update_board()

    # Changer de joueur
    current_player = "b" if current_player == "w" else "w"

# Mettre à jour l'affichage du plateau
def update_board():
    canvas.delete("piece")
    draw_pieces()

# Création du canvas (plateau de jeu)
canvas = tk.Canvas(root, width=COLS * SQUARE_SIZE, height=ROWS * SQUARE_SIZE)
canvas.pack()

# Dessiner le plateau et les pièces initiales
draw_board()
draw_pieces()

# Gérer les clics sur le plateau
canvas.bind("<Button-1>", on_square_click)

# Lancer la fenêtre Tkinter
root.mainloop()
