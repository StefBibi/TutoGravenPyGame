# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:12:59 2021

@author: Matymate
"""

import pygame
import random

# creation classe pour representer la notion de monstre
# et qui herite de Sprite pour etre un element graphique
class Monster(pygame.sprite.Sprite):
    
    
    # constructeur et attributs
    def __init__(self, game):
        # constructeur classe parent
        super().__init__()
        # attributs Monster
        self.health = 95
        self.max_health = 100
        self.attack = 1
        self.velocity = random.randint(1,2)
        # memorise le Game dans le Player
        self.game = game
        # definit un fichier a l'image
        self.image = pygame.image.load('assets/mummy.png')
        # definit un rectangle selon l'image chargee
        self.rect = self.image.get_rect()
        # definit une position de depart de l'image
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540


    # methode pour infliger des degats
    # avec en argument la perte de pv
    def damage(self, damage):
        # enleve des pv
        self.health -= damage
        # si PV a zero, reapparait comme un 
        #nouveau monstre (astuce pour optimiser mémoire)
        if self.health <= 0:
            # reapparait a son origine
            self.health = 90
            self.velocity = random.randint(1,2)
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = 540
            
            # si la barre des comete est full
            if self.game.comet_event.is_full():
                # retire le monstre du jeu
                self.game.all_monsters.remove(self)
                   
                # tentative declenchement des cometes
                self.game.comet_event.attempt_fall()


    # methode pour gerer la barre de vie avec en argument
    # une surface sur laquelle dessiner (= l'ecran)
    def update_health_bar(self, surface):
        # RGB couleur pour la barre de vie
        bar_color = (110,210,45)
        # RGB couleur pour arriere plan de la barre
        back_bar_color = (60,60,60)
        # [x, y, w, h] position, largeur et hauteur de la barre de vie 
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        # [x, y, w, h] position, largeur et hauteur de l'arriere plan de la barre 
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        # dessine l'arriere plan de la barre sur la surface
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # dessine la jauge de vie sur la surface
        pygame.draw.rect(surface, bar_color, bar_position)


    # methode de deplacement monstre gauche
    def forward(self):
        # Si monstre n'est pas en collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # sinon le monstre est en collision et attque le joueur
        else:
            self.game.player.damage(self.attack)
            