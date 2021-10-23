# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:56:22 2021

@author: Matymate
"""
import pygame
# import la classe Projectile du script projectile.py
from projectile import Projectile

# creation classe pour representer le joueur
# et qui herite de Sprite pour etre un element graphique
class Player(pygame.sprite.Sprite):
    
    # constructeur avec argument et attributs
    def __init__(self, game):
        # constructeur classe parent
        super().__init__()
        # attribut Player
        self.health = 100
        self.max_health = 100
        self.attack = 20 
        self.velocity = 5
        # memorise le Game dans le Player
        self.game = game
        # cree un groupe pour gerer les projectiles
        self.all_projectiles = pygame.sprite.Group()
        # definit un fichier a l'image
        self.image = pygame.image.load('assets/player.png')
        # definit un rectangle selon l'image chargee
        self.rect = self.image.get_rect()
        # definit une position de depart de l'image
        self.rect.x = 400
        self.rect.y = 500
        
        
    # methode pour infliger des degats
    # avec en argument la perte de pv
    def damage(self, damage):
        if self.health - damage > damage:
            self.health -= damage
        else:
            self.game.game_over()
        
        
    # methode pour gerer la barre de vie avec en argument
    # une surface sur laquelle dessiner (= l'ecran)
    def update_health_bar(self, surface):
        # dessine l'arriere plan de la barre sur la surface
        pygame.draw.rect(surface, (60,60,60), [self.rect.x + 50, self.rect.y + 10, self.max_health, 5])
        # dessine la jauge de vie sur la surface
        pygame.draw.rect(surface, (110,210,45), [self.rect.x + 50, self.rect.y + 10, self.health, 5])
                    
        
    # methode qui lance un projectile du joueur
    def launch_projectile(self):
        # instanciation du projectile et passe le parent en arg
        projectile = Projectile(self)
        # ajoute le projectile au groupe de projectile
        self.all_projectiles.add(projectile)
        
        
    # methode de deplacment joueur droite
    def move_right(self):
        # Si joueur n'est pas en collision avec un monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
    # methode de deplacment joueur gauche
    def move_left(self):
        self.rect.x -= self.velocity
        