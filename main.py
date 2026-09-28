# initialisation -----------------------------------------------------------------------------------------------------------------------------------------------------------
import keyboard
import pygame
import math

orbit_distance = 50

# --- LISTE DES ATOMES ([x, y]) ---
atoms = [
    [640, 360],
    [300, 200],
    [950, 500],
    [250, 550]
]

# Initialisation automatique de l'angle pour chaque atome de la liste
for atom in atoms:
    atom.append(0.0)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# functions and loop -------------------------------------------------------------------------------------------------------------------------------------------------------
def colorpicker(charge):
    if charge == -1 :
        r = 2
        color = (0,255,255)
        return r, color
    elif charge == 1 :
        r = 10
        color = (255,0,0)
        return r, color
    else :
        color = (122,122,122)
        return color
    

while True:
  screen.fill("black")

  # Boucle pour afficher chaque atome de la liste
  for atom in atoms:
      center_x = atom[0]
      center_y = atom[1]
      
      # 1. Dessiner l'outline de la trajectoire
      pygame.draw.circle(screen, (50, 50, 50), (center_x, center_y), orbit_distance, 1)

      # 2. Dessiner le proton au centre (charge par défaut = 1)
      r_red, color_red = colorpicker(1)
      pygame.draw.circle(screen, color_red, (center_x, center_y), r_red)

      # 3. Calculer la position de l'électron en orbite
      r_blue, color_blue = colorpicker(-1)
      blue_x = center_x + orbit_distance * math.cos(atom[2])
      blue_y = center_y + orbit_distance * math.sin(atom[2])

      # Dessiner l'électron
      pygame.draw.circle(screen, color_blue, (int(blue_x), int(blue_y)), r_blue)

      # Faire avancer l'angle de cet électron pour la prochaine image
      atom[2] += 0.1

  pygame.display.flip()

  if keyboard.is_pressed("q"):
    pygame.quit()
    break

  # Limiter à 60 images par seconde pour une vitesse stable
  clock.tick(60)