import pygame
import math
import random
import numpy as np

# --- Configuration et variables ---
WIDTH, HEIGHT = 1280, 720
orbit_distance = 25.0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- Listes globales ---
atoms = []
waves = []

# Initialisation des atomes en cercle au centre (comme dans le C++ de Kavan)
num_atoms = 15
radius_cluster = 100.0
center_screen = np.array([WIDTH / 2.0, HEIGHT / 2.0])

for i in range(num_atoms):
    angle = 2.0 * math.pi * i / num_atoms
    x = math.cos(angle) * radius_cluster + center_screen[0]
    y = math.sin(angle) * radius_cluster + center_screen[1]
    
    # Structure d'un atome : [pos_x, pos_y, v_x, v_y, electron_angle, n, excited_timer]
    atoms.append([x, y, 0.0, 0.0, 0.0, 1, 0.0])

# --- Fonction de couleur selon la charge ---
def colorpicker(charge):
    if charge == -1:
        return 2, (0, 255, 255)  # Électron (Cyan)
    elif charge == 1:
        return 5, (255, 0, 0)    # Proton (Rouge)
    else:
        return 5, (128, 128, 128)

# --- Initialisation de quelques vagues initiales ---
energyN1toN2 = -13.6 / (2 * 2) - (-13.6)
for i in range(24):
    wave_pos = np.array([200.0 + center_screen[0], i * 20 - 200 + center_screen[1]])
    wave_dir = np.array([-1.0, 0.0])
    
    # Structure d'une vague : [energy, pos, dir, col, sigma, k, phase, a, points]
    points = []
    for x in np.arange(-40.0, 40.1, 0.1):
        points.append(wave_pos + x * wave_dir)
        
    waves.append({
        "energy": energyN1toN2,
        "pos": wave_pos,
        "dir": wave_dir,
        "col": (0, 255, 255),
        "phase": 0.0,
        "a": 10.0,
        "k": 0.4,
        "points": points
    })

# --- Boucle principale ---
running = True
while running:
    dt = 0.016 # delta temps approximatif pour 60 FPS
    
    # Gestion des événements (clavier / souris / fermeture)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Clic gauche
                mx, my = pygame.mouse.get_pos()
                spawn_pos = np.array([float(mx), float(my)])
                
                # Émettre 25 vagues dans toutes les directions au clic
                for _ in range(25):
                    angle = random.uniform(0, 2 * math.pi)
                    dir_vec = np.array([math.cos(angle), math.sin(angle)])
                    
                    points = []
                    for x in np.arange(-40.0, 40.1, 0.1):
                        points.append(spawn_pos + x * dir_vec)
                        
                    waves.append({
                        "energy": energyN1toN2,
                        "pos": spawn_pos,
                        "dir": dir_vec,
                        "col": (0, 255, 255),
                        "phase": 0.0,
                        "a": 10.0,
                        "k": 0.4,
                        "points": points
                    })

    # Touche 'q' pour quitter aussi
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    screen.fill((0, 0, 0))

    # --- 1. Mise à jour et affichage des atomes / interactions ---
    for i, a in enumerate(atoms):
        pos_a = np.array([a[0], a[1]])
        v_a = np.array([a[2], a[3]])

        # Répulsion entre les atomes
        for j, a2 in enumerate(atoms):
            if i == j:
                continue
            pos_a2 = np.array([a2[0], a2[1]])
            diff = pos_a - pos_a2
            dist = np.linalg.norm(diff)
            if dist > 0.001:
                dir_rep = diff / dist
                v_a += dir_rep / dist * 500.0  # Force de répulsion

        # Répulsion des bords de l'écran
        boundary_stiffness = 0.1
        boundary_threshold = 150.0
        if pos_a[0] < boundary_threshold:
            v_a[0] += (boundary_threshold - pos_a[0]) * boundary_stiffness
        if pos_a[0] > WIDTH - boundary_threshold:
            v_a[0] -= (pos_a[0] - (WIDTH - boundary_threshold)) * boundary_stiffness
        if pos_a[1] < boundary_threshold:
            v_a[1] += (boundary_threshold - pos_a[1]) * boundary_stiffness
        if pos_a[1] > HEIGHT - boundary_threshold:
            v_a[1] -= (pos_a[1] - (HEIGHT - boundary_threshold)) * boundary_stiffness

        # Appliquer vitesse et amortissement
        pos_a += v_a * dt
        v_a *= 0.95  # Damping

        # Mettre à jour les coordonnées de l'atome
        a[0], a[1] = pos_a[0], pos_a[1]
        a[2], a[3] = v_a[0], v_a[1]

        # --- Dessin du Proton (centre) ---
        r_prot, col_prot = colorpicker(1)
        pygame.draw.circle(screen, col_prot, (int(pos_a[0]), int(pos_a[1])), r_prot)

        # --- Gestion de l'Électron et de son orbite ---
        n = a[5]
        lvl = n * orbit_distance
        
        # Dessiner l'orbite (cercle gris)
        pygame.draw.circle(screen, (70, 70, 70), (int(pos_a[0]), int(pos_a[1])), int(lvl), 1)

        # Mettre à jour l'angle de l'électron
        a[4] += 0.05
        elec_angle = a[4]
        
        elec_x = pos_a[0] + lvl * math.cos(elec_angle)
        elec_y = pos_a[1] + lvl * math.sin(elec_angle)
        elec_pos = np.array([elec_x, elec_y])

        # Timer d'excitation
        if a[6] > 0.0:
            a[6] -= 0.001
        else:
            # Désexcitation spontanée (l'électron redescend de niveau et émet une vague)
            if n > 1:
                a[5] -= 1
                a[6] += 0.003
                wave_dir_rnd = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
                norm_wd = np.linalg.norm(wave_dir_rnd)
                if norm_wd > 0:
                    wave_dir_rnd /= norm_wd
                
                energyDiff = -13.6 / ((n) * (n)) - (-13.6 / ((n - 1) * (n - 1)))
                
                points_dec = []
                for x in np.arange(-40.0, 40.1, 0.1):
                    points_dec.append(elec_pos + x * wave_dir_rnd)
                
                waves.append({
                    "energy": abs(energyDiff),
                    "pos": elec_pos,
                    "dir": wave_dir_rnd,
                    "col": (255, 255, 0), # Jaune pour l'émission photonique/vague
                    "phase": 0.0,
                    "a": 10.0,
                    "k": 0.4,
                    "points": points_dec
                })

        # Collision entre l'électron et les vagues (Absorption pour monter en niveau)
        for wave in waves:
            if wave["energy"] == 0.0:
                continue
            energy_for_up = -13.6 / ((n + 1) * (n + 1)) - (-13.6 / (n * n))
            
            for wp in wave["points"]:
                dist_to_wp = np.linalg.norm(elec_pos - wp)
                if dist_to_wp < 20.0 and abs(wave["energy"] - abs(energy_for_up)) < 1.0 and wave["col"] != (255, 255, 0):
                    wave["energy"] = 0.0  # Absorbe la vague
                    a[5] += 1             # Monte d'un niveau d'énergie (n++)
                    a[6] += 0.003
                    break

        # Dessiner l'électron
        r_elec, col_elec = colorpicker(-1)
        pygame.draw.circle(screen, col_elec, (int(elec_pos[0]), int(elec_pos[1])), r_elec)

    # --- 2. Mise à jour et affichage des Vagues ---
    for wave in waves[:]:
        if wave["energy"] == 0.0:
            waves.remove(wave)
            continue
            
        wave["phase"] += 30.0 * dt
        
        # Déplacement et rendu des points de la vague
        drawn_points = []
        out_of_bounds = True
        
        for p in wave["points"]:
            # Déplacer le point le long de sa direction
            p += wave["dir"] * (200.0 * dt)
            
            # Vérifier si la vague est toujours dans l'écran
            if -100 <= p[0] <= WIDTH + 100 and -100 <= p[1] <= HEIGHT + 100:
                out_of_bounds = False
            
            # Calcul du déplacement sinusoïdal perpendiculaire
            perp = np.array([-wave["dir"][1], wave["dir"][0]])
            norm_perp = np.linalg.norm(perp)
            if norm_perp > 0:
                perp /= norm_perp
                
            y_disp = wave["a"] * math.sin(wave["k"] * np.linalg.norm(p - wave["pos"]) - wave["phase"])
            draw_pos = p + perp * y_disp
            drawn_points.append((int(draw_pos[0]), int(draw_pos[1])))

        if out_of_bounds:
            waves.remove(wave)
            continue

        # Dessiner la ligne de la vague avec Pygame
        if len(drawn_points) > 1:
            pygame.draw.aalines(screen, wave["col"], False, drawn_points)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()