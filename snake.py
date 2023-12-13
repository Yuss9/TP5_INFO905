import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de l'écran
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Dimensions d'une cellule
cell_size = 20

# Vitesse du serpent
snake_speed = 10

# Définition des polices
font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 24)

# Fonction pour afficher le score


def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

# Fonction pour afficher le message de fin de partie


def game_over_restart(score):
    game_over_text = font.render("Game Over", True, white)
    score_text = font.render("Score: " + str(score), True, white)
    restart_text = font.render(
        "Press 'R' to restart / any key to exit", True, white)
    screen.blit(game_over_text, (width/2 - game_over_text.get_width() /
                2, height/2 - game_over_text.get_height()))
    screen.blit(score_text, (width/2 - score_text.get_width()/2, height/2))
    screen.blit(restart_text, (width/2 - restart_text.get_width() /
                2, height/2 + restart_text.get_height()))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                else:
                    return False
# Fonction principale pour exécuter le jeu


def game():
    # Position initiale du serpent
    snake_x = width / 2
    snake_y = height / 2

    # Déplacements initiaux
    dx = 0
    dy = 0

    # Liste des segments du serpent
    snake_segments = []
    snake_length = 1

    # Position initiale de la nourriture
    food_x = round(random.randrange(
        0, width - cell_size) / cell_size) * cell_size
    food_y = round(random.randrange(
        0, height - cell_size) / cell_size) * cell_size

    # Score
    score = 0

    # Booléen pour déterminer si le jeu est en cours ou terminé
    game_over = False

    # Boucle principale du jeu
    while not game_over:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != cell_size:
                    dx = -cell_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx != -cell_size:
                    dx = cell_size
                    dy = 0
                elif event.key == pygame.K_UP and dy != cell_size:
                    dx = 0
                    dy = -cell_size
                elif event.key == pygame.K_DOWN and dy != -cell_size:
                    dx = 0
                    dy = cell_size
                elif event.key == pygame.K_r and game_over:
                    # Redémarrage de la partie
                    game()

        # Mise à jour de la position du serpent
        snake_x += dx
        snake_y += dy

        # Vérification des collisions avec les bords de l'écran
        if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
            game_over = True

        # Vérification des collisions avec le corps du serpent
        for segment in snake_segments[1:]:
            if segment == [snake_x, snake_y]:
                game_over = True

        # Vérification de la collision avec la nourriture
        if snake_x == food_x and snake_y == food_y:
            # Augmentation du score et de la longueur du serpent
            score += 10
            snake_length += 1

            # Génération d'une nouvelle position pour la nourriture
            food_x = round(random.randrange(
                0, width - cell_size) / cell_size) * cell_size
            food_y = round(random.randrange(
                0, height - cell_size) / cell_size) * cell_size

        # Mise à jour de la liste des segments du serpent
        snake_segments.insert(0, [snake_x, snake_y])

        # Suppression des segments supplémentaires si la longueur du serpent a dépassé snake_length
        if len(snake_segments) > snake_length:
            snake_segments.pop()

        # Effacement de l'écran
        screen.fill(black)

        # Affichage du serpent
        for segment in snake_segments:
            pygame.draw.rect(
                screen, white, (segment[0], segment[1], cell_size, cell_size))

        # Affichage de la nourriture
        pygame.draw.rect(screen, red, (food_x, food_y, cell_size, cell_size))

        # Affichage du score
        show_score(score)

        # Vérification de la fin de partie
        if game_over:
            if game_over_restart(score):
                game()
            else:
                pygame.quit()
            return

        # Mise à jour de l'écran
        pygame.display.update()

        # Contrôle de la vitesse du jeu
        pygame.time.Clock().tick(snake_speed)

    # Quitter Pygame
    pygame.quit()


# Exécution du jeu
game()
