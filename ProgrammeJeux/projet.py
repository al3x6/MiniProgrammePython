import tkinter as tk
import random

# DEFINITION DES CONSTANTES
FPRO = random.randint(1, 40)
EPRE = random.randint(1, 30)
DPRO = random.randint(1, 20)
DPRE = random.randint(1, 20)
C = 30
NB_CASE_X = NB_CASE_Y = 30
L, H = C * NB_CASE_X, C * NB_CASE_Y
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# DEFINITION DES LISTES ET DICTIONNAIRES
pro_age, pro_obj = {}, {}
pre_age, pre_obj = {}, {}
pos_proie = []
pos_predateur = []

# ATTRIBUTION DU NOMBRE DE TOUR
nb_tour, tour = 50, 0

# Création de la fenêtre et du canevas avec Tkinter
root = tk.Tk()
root.title("Simulation Proies/Prédateurs")
canvas = tk.Canvas(root, width=L, height=H, bg="black")
canvas.pack()

# CONSTRUCTION DU PLATEAU
def dessine_plateau():
    """Crée le tableau avec les lignes du quadrillage."""
    for x in range(0, L, C):
        canvas.create_line(x, 0, x, H, fill="white")
    for y in range(0, H, C):
        canvas.create_line(0, y, L, y, fill="white")

# CENTRALISATION DES PROIES/PREDATEURS
def case_2_pixel(col, lig):
    """Convertit les coordonnées d'une case en pixels."""
    return col * C + C // 2, lig * C + C // 2

# INITIALISATION DES DICTIONNAIRES
def init_data(pro_age, pro_obj):
    """Initialise les dictionnaires des âges et des objets pour les cases."""
    for lig in range(NB_CASE_Y):
        for col in range(NB_CASE_X):
            pro_age[(lig, col)] = 0
            pro_obj[(lig, col)] = None

# NETTOYAGE DE CASE
def efface_case(lig, col, pro_age, pro_obj):
    """Efface la case graphiquement."""
    if pro_obj[(lig, col)] is None:
        return
    canvas.delete(pro_obj[(lig, col)])
    pro_obj[(lig, col)] = None
    pro_age[(lig, col)] = 0

# NAISSANCE D'UNE PROIE
def naissance_une_proie(pro_age, pro_obj):
    """Fait naître une proie à une position aléatoire."""
    lig, col = random.randint(0, NB_CASE_Y - 1), random.randint(0, NB_CASE_X - 1)
    if pro_obj[(lig, col)] is not None:
        return None
    y, x = case_2_pixel(lig, col)
    proie = canvas.create_oval(x - C // 2, y - C // 2, x + C // 2, y + C // 2, fill="green")
    pro_obj[(lig, col)] = proie
    pro_age[(lig, col)] = DPRO
    return proie

# NAISSANCE D'UN PREDATEUR
def naissance_un_predateur(pre_age, pre_obj):
    """Fait naître un prédateur à une position aléatoire."""
    lig, col = random.randint(0, NB_CASE_Y - 1), random.randint(0, NB_CASE_X - 1)
    if pre_obj[(lig, col)] is not None:
        return None
    y, x = case_2_pixel(lig, col)
    predateur = canvas.create_oval(x - C // 2, y - C // 2, x + C // 2, y + C // 2, fill="red")
    pre_obj[(lig, col)] = predateur
    pre_age[(lig, col)] = EPRE
    return predateur

# MISE À JOUR DU CANEVAS
def mise_a_jour():
    global tour
    if tour < nb_tour:
        for i in range(FPRO):
            naissance_une_proie(pro_age, pro_obj)
        for i in range(EPRE):
            naissance_un_predateur(pre_age, pre_obj)
        
        # Rafraîchit la fenêtre
        root.update()
        
        tour += 1
        root.after(500, mise_a_jour)

# Lancer la simulation
dessine_plateau()
init_data(pro_age, pro_obj)
init_data(pre_age, pre_obj)
mise_a_jour()

root.mainloop()