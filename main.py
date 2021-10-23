# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 21:10:30 2021

@author: Matymate
"""
import time
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

# instanciation du Jeu
game = Game()

running=True

# Boucle d'affichage
while running:
    # sinon move trop rapide
    time.sleep(0.010)
    
    # injecte l'image dans l'ecran et la positionne
    screen.blit(background, (0,-200))
    
    # applique l'image du joueur dans l'ecran et la positionne
    screen.blit(game.player.image, game.player.rect)
    # actualise la barre de vie du joueur et l'affiche
    game.player.update_health_bar(screen)

    # recupe les projectiles du joueur et les gere
    for projectile in game.player.all_projectiles:
        projectile.move()
        
    # applique le groupe de projectiles a l'ecran
    game.player.all_projectiles.draw(screen)
        
    # recupe les monstre du jeu et les gere
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
            
    # applique le groupe de monstree a l'ecran
    game.all_monsters.draw(screen)
    
    # verifie si joueur se deplace a droite et dans limite
    if game.pressed.get(pygame.K_RIGHT) and (game.player.rect.x + game.player.rect.width) < screen.get_width():
        game.player.move_right()
    # verifie si joueur se deplace a gauche et dans limite
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    
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
    