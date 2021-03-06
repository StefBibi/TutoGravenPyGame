# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:57:52 2021

@author: Matymate
"""

import pygame

# import la classe Player du script player.py
from player import Player
# import la classe Monster du script monster.py
from monster import Mummy, Alien
# import la classe CometFallEvent du script comet_event.py
from comet_event import CometFallEvent
# import la classe SoundManager
from sounds import SoundManager

# creation classe pour gerer notre jeu
class Game:
    
    # constructeur et attributs
    def __init__(self):
        # var pour indiquer si Game a commence ou non
        self.is_playing = False # False
        # instanciation du joueur et passe Game(=self) en argument
        self.player = Player(self)
        # groupe de un seul player pour y ranger player
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        # dictionnaire pour stocker touche active
        self.pressed = {}
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # genere evenement des comete et passe l'instance de game
        self.comet_event = CometFallEvent(self)
        # mettre score a 0
        self.font = pygame.font.Font("assets/PottaOne-Regular.ttf",24)
        self.score = 0
        # initialise la gestion des sons
        self.sound_manager = SoundManager()

    # methode pour ajouter des points au score
    def add_score(self, points=10):
        self.score += points

        
    # methode pour lancer le jeu et initialiser les monstres
    def start(self):
        self.is_playing = True
        # genere un monstre Mummy et un second
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        # genere un monstre Alien
        self.spawn_monster(Alien)
    
    # methode pour creer un monstre Mummy, Alien ....
    def spawn_monster(self, monster_class_name):
        #monster = Mummy(self)
        monster = monster_class_name.__call__(self)
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
        # RAZ : zero monstre, zero comete
        # reinitialise joueur et ecran d'accueil
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.rect.x = 400
        self.player.rect.y = 500
        self.is_playing = False
        self.comet_event.reset_percent()
        self.score = 0
        # joue le son
        self.sound_manager.play('game_over')
        
    
    # methode pour gerer les elements du jeu et les
    # afficher a l'ecran
    def update(self, screen):
        # afficher le scrore a l'ecran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        
        # applique l'image du joueur dans l'ecran et la positionne
        screen.blit(self.player.image, self.player.rect)
        # actualise la barre de vie du joueur et l'affiche
        self.player.update_health_bar(screen)
        # actualise l'animation du joueur
        self.player.update_animation()
        
        # actualise la barre de charge des cometes
        self.comet_event.update_bar(screen)
    
        # recupe les projectiles du joueur et les gere
        for projectile in self.player.all_projectiles:
            projectile.move()
            
        # applique le groupe de projectiles a l'ecran
        self.player.all_projectiles.draw(screen)
            
        # recupe les monstre du jeu et les gere
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
                
        # applique le groupe de monstre a l'ecran
        self.all_monsters.draw(screen)
        
        # recupe les cometes du jeu et les gere
        for comet in self.comet_event.all_comets:
            comet.fall()
        
        # applique le groupe de comete a l'ecran
        self.comet_event.all_comets.draw(screen)
        
        # verifie si joueur se deplace a droite et dans limite
        if self.pressed.get(pygame.K_RIGHT) and (self.player.rect.x + self.player.rect.width) < screen.get_width():
            self.player.move_right()
        # verifie si joueur se deplace a gauche et dans limite
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        