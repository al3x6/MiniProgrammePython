import pygame
import random

# Paramètres de la fenêtre
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE

# Couleurs
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Habitants
BLUE = (0, 0, 255)   # Voitures
RED = (255, 0, 0)    # Maisons
BLACK = (0, 0, 0)    # Couleur de la grille

class Habitants:
    def __init__(self, nom):
        self.nom = nom
        self.position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    
    def deplacer(self):
        x, y = self.position
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])  # Déplacement aléatoire
        self.position = (max(0, min(GRID_SIZE - 1, x + dx)), max(0, min(GRID_SIZE - 1, y + dy)))

class Maison:
    def __init__(self, position):
        self.position = position

class Voiture:
    def __init__(self, position):
        self.position = position

class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Simulation de Vie")
        
        self.habitants = [Habitants(f'Habitant {i+1}') for i in range(5)]
        self.maisons = [Maison((random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))) for _ in range(3)]
        self.voitures = [Voiture((random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))) for _ in range(2)]
        
        self.clock = pygame.time.Clock()
        self.running = True

    def mettre_a_jour(self):
        for habitant in self.habitants:
            habitant.deplacer()
    
    def afficher(self):
        self.screen.fill(WHITE)
        
        # Dessiner la grille
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, BLACK, (0, y), (WIDTH, y))

        # Afficher les habitants
        for habitant in self.habitants:
            x, y = habitant.position
            pygame.draw.circle(self.screen, GREEN, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

        # Afficher les maisons
        for maison in self.maisons:
            x, y = maison.position
            pygame.draw.rect(self.screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        # Afficher les voitures
        for voiture in self.voitures:
            x, y = voiture.position
            pygame.draw.rect(self.screen, BLUE, (x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2))

        # Légende
        font = pygame.font.Font(None, 36)
        legend_surface = font.render("Légende: Verts - Habitants, Rouges - Maisons, Bleus - Voitures", True, BLACK)
        self.screen.blit(legend_surface, (10, HEIGHT - 40))

        pygame.display.flip()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.mettre_a_jour()
            self.afficher()
            self.clock.tick(5)  # Limite la simulation à 5 mises à jour par seconde

        pygame.quit()

# Lancer la simulation
simulation = Simulation()
simulation.run()
