# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 21:10:30 2021

@author: Matymate
"""
import time
import math
# import la lib pygame
import pygame
# import la classe Game du script game.py
from game import Game

# initialise la lib pygame
pygame.init()

# titre de la fenetre
pygame.display.set_caption('Commet fall game')
# dimensionne l'ecran et le met dans une var
screen = pygame.display.set_mode((1080, 720))

# definit une image
background = pygame.image.load('assets/bg.jpg')

# importer baniere debut du jeu
banner = pygame.image.load('assets/banner.png')
# redimension (en ecrasant)
banner = pygame.transform.scale(banner, (500, 500))
# recupe le rectangle associé a l'image
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

# importe un bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

# instanciation du Jeu
game = Game()

running=True

# Boucle d'affichage
while running:
    # sinon move trop rapide
    time.sleep(0.010)
    
    # injecte l'image dans l'ecran et la positionne
    screen.blit(background, (0,-200))
    
    # si le jeu a bien débuté
    if game.is_playing:
        # methode pour gerer les elements du jeu et les
        # afficher a l'ecran
        game.update(screen)
    else:
        # ajout ecran de bienvenue et un bouton de lancement
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
    
    # rafraichit l'ecran
    pygame.display.flip()
    
    # gestion d'evenement
    for event in pygame.event.get():
        # si bouton quit
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        # sinon touche du clavier appuyée
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            #detecte si touche espace appuyée pour lancer projectile
            if event.key ==  pygame.K_SPACE:
                game.player.launch_projectile()

        # sinon touche du clavier lachée
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        # sinon clic de la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verifi si souris en collision avec bouton de lancement
            if play_button_rect.collidepoint(event.pos):
                # lancement du jeu
                game.start()
    