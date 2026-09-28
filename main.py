import keyboard
import pygame

# initialisation------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((1280, 720))
while True :
    
    if keyboard.is_pressed('q'):
        pygame.quit()