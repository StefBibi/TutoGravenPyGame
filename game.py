# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:57:52 2021

@author: Matymate
"""

import pygame

# import la classe Player du script player.py
from player import Player
# import la classe Monster du script monster.py
from monster import Monster

# creation classe pour gerer notre jeu
class Game:
    
    # constructeur et attributs
    def __init__(self):
        # instanciation du joueur et passe Game en argument
        self.player = Player(self)
        # groupe de un seul player pour y ranger player
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        # dictionnaire pour stocker touche active
        self.pressed = {}
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # genere un monstre et un second
        self.spawn_monster()
        self.spawn_monster()
    
    # methode pour creer un monstre
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        
    # methode pour verifier collision entre un sprite (Player/Monster/Projectile)
    # et un groupe de Sprite (all_monsters/all_players)
    # retourne une liste de ce qui est en collision
    def check_collision(self, sprite, group):
        # False : pour ne pas doKill le Sprite player
        # Hitbox : pygame.sprite.collide_mask
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        