import tkinter as tk
from tkinter import messagebox

# Fenêtre principale
root = tk.Tk()
root.title("Jeu de Morpion")

# Variables globales
current_player = "X"
board = [""] * 9  # Grille de 3x3, initialement vide

# Fonction pour vérifier si un joueur a gagné
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]  # Renvoie le gagnant ("X" ou "O")
    if "" not in board:
        return "Draw"  # Match nul
    return None  # Pas encore de gagnant

# Fonction pour gérer les clics sur les boutons
def button_click(index):
    global current_player

    # Si la case est déjà occupée, on ne fait rien
    if board[index] != "":
        return

    # Marque le coup du joueur
    board[index] = current_player
    buttons[index].config(text=current_player, state="disabled")

    # Vérifie si quelqu'un a gagné
    winner = check_winner()
    if winner:
        if winner == "Draw":
            messagebox.showinfo("Match nul", "C'est un match nul!")
        else:
            messagebox.showinfo("Victoire!", f"Le joueur {winner} a gagné!")
        reset_board()
    else:
        # Change de joueur
        current_player = "O" if current_player == "X" else "X"

# Fonction pour réinitialiser la grille
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="", state="normal")

# Création des boutons pour le plateau de jeu
buttons = []
for i in range(9):
    button = tk.Button(root, text="", width=10, height=3, font=('Helvetica', 20), command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Lancement de l'application
root.mainloop()
