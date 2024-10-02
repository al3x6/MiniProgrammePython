import pygame
import random
import matplotlib.pyplot as plt

# Initialisation de Pygame
pygame.init()

# Constantes du jeu
TAILLE_ECRAN = 600  # Taille de la fenêtre (600x600 pixels)
TAILLE_CELLULE = 10  # Taille d'une cellule (10x10 pixels)
GRILLE_TAILLE = TAILLE_ECRAN // TAILLE_CELLULE  # Grille 60x60
FPS = 5  # Nombre d'images par seconde

# Couleurs
COULEUR_VIDE = (0, 0, 0)        # noir pour le fond
COULEUR_GRILLE = (200, 200, 200)      # Gris clair pour la grille
COULEUR_HABITANT = (0, 255, 0)        # Vert pour les habitants
COULEUR_TEXTE = (0, 0, 0)             # Noir pour le texte

# Fenêtre de jeu
ecran = pygame.display.set_mode((TAILLE_ECRAN, TAILLE_ECRAN))
pygame.display.set_caption("Simulation de Vie")

# Police pour les statistiques
police_stats = pygame.font.SysFont('Arial', 16)

# Modèle d'agent
class Habitants:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reproduction_tours = 3

    def se_deplacer(self):
        direction = random.choice(['haut', 'bas', 'gauche', 'droite'])
        if direction == 'haut' and self.y > 0:
            self.y -= 1
        elif direction == 'bas' and self.y < GRILLE_TAILLE - 1:
            self.y += 1
        elif direction == 'gauche' and self.x > 0:
            self.x -= 1
        elif direction == 'droite' and self.x < GRILLE_TAILLE - 1:
            self.x += 1

    def se_reproduire(self, grille):
        if self.reproduction_tours <= 0:
            adjacents = [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]
            random.shuffle(adjacents)
            for nx, ny in adjacents:
                if 0 <= nx < GRILLE_TAILLE and 0 <= ny < GRILLE_TAILLE and grille[nx][ny] is None:
                    grille[nx][ny] = Habitants(nx, ny)
                    self.reproduction_tours = 3  # Reset le compteur
                    break
        else:
            self.reproduction_tours -= 1

# Initialisation de la grille
grille = [[None for _ in range(GRILLE_TAILLE)] for _ in range(GRILLE_TAILLE)]

# Placement initial des habitants
nombre_habitants = 100
for _ in range(nombre_habitants):
    x, y = random.randint(0, GRILLE_TAILLE - 1), random.randint(0, GRILLE_TAILLE - 1)
    while grille[x][y] is not None:
        x, y = random.randint(0, GRILLE_TAILLE - 1), random.randint(0, GRILLE_TAILLE - 1)
    grille[x][y] = Habitants(x, y)

# Boucle principale du jeu
habitants_history = []
running = True
horloge = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour de la grille (déplacement et interactions)
    nouvelle_grille = [[None for _ in range(GRILLE_TAILLE)] for _ in range(GRILLE_TAILLE)]
    nombre_habitants_vivants = 0
    
    for x in range(GRILLE_TAILLE):
        for y in range(GRILLE_TAILLE):
            agent = grille[x][y]
            if isinstance(agent, Habitants):
                agent.se_deplacer()
                agent.se_reproduire(nouvelle_grille)
                nouvelle_grille[agent.x][agent.y] = agent
                nombre_habitants_vivants += 1

    grille = nouvelle_grille

    # Enregistrer les statistiques
    habitants_history.append(nombre_habitants_vivants)

    # Affichage de la grille
    ecran.fill(COULEUR_VIDE)

    # Dessiner les agents
    for x in range(GRILLE_TAILLE):
        for y in range(GRILLE_TAILLE):
            agent = grille[x][y]
            rect = pygame.Rect(x * TAILLE_CELLULE, y * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE)
            if isinstance(agent, Habitants):
                pygame.draw.rect(ecran, COULEUR_HABITANT, rect)

    # Dessiner la grille
    for x in range(0, TAILLE_ECRAN, TAILLE_CELLULE):
        pygame.draw.line(ecran, COULEUR_GRILLE, (x, 0), (x, TAILLE_ECRAN))
    for y in range(0, TAILLE_ECRAN, TAILLE_CELLULE):
        pygame.draw.line(ecran, COULEUR_GRILLE, (0, y), (TAILLE_ECRAN, y))

    # Afficher les statistiques
    texte_stats = police_stats.render(f"Habitants: {nombre_habitants_vivants}", True, COULEUR_TEXTE)
    ecran.blit(texte_stats, (10, 10))

    pygame.display.flip()
    horloge.tick(FPS)

pygame.quit()

# Création du graphe
plt.plot(habitants_history, label='Habitants', color='green')
plt.title('Dynamique des Habitants')
plt.xlabel('Tours')
plt.ylabel('Nombre')
plt.legend()
plt.show()
