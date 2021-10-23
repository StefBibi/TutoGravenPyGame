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
        # var pour indiquer si Game a commence ou non
        self.is_playing = False
        # instanciation du joueur et passe Game(=self) en argument
        self.player = Player(self)
        # groupe de un seul player pour y ranger player
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        # dictionnaire pour stocker touche active
        self.pressed = {}
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()

        
    # methode pour lancer le jeu et initialiser les monstres
    def start(self):
        self.is_playing = True
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
    
    
    # methode pour reinitialiser game si over
    def game_over(self):
        # RAZ : zero monstre, reinitialise joueur et ecran d'accueil
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.rect.x = 400
        self.player.rect.y = 500
        self.is_playing = False
        
    
    # methode pour gerer les elements du jeu et les
    # afficher a l'ecran
    def update(self, screen):
        # applique l'image du joueur dans l'ecran et la positionne
        screen.blit(self.player.image, self.player.rect)
        # actualise la barre de vie du joueur et l'affiche
        self.player.update_health_bar(screen)
    
        # recupe les projectiles du joueur et les gere
        for projectile in self.player.all_projectiles:
            projectile.move()
            
        # applique le groupe de projectiles a l'ecran
        self.player.all_projectiles.draw(screen)
            
        # recupe les monstre du jeu et les gere
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
                
        # applique le groupe de monstree a l'ecran
        self.all_monsters.draw(screen)
        
        # verifie si joueur se deplace a droite et dans limite
        if self.pressed.get(pygame.K_RIGHT) and (self.player.rect.x + self.player.rect.width) < screen.get_width():
            self.player.move_right()
        # verifie si joueur se deplace a gauche et dans limite
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        