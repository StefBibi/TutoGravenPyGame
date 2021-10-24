# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:36:38 2021

@author: Matymate
"""

import pygame
import random

# creer classe pour gerer une comete
# et qui herite de Sprite pour etre un element graphique
class Comet(pygame.sprite.Sprite):
    
    # constructeur
    def __init__(self, comet_event):
        # constructeur classe parent
        super().__init__()
        # attribut Comet
        self.velocity = random.randint(1,2)
        self.comet_event = comet_event
        # definit un fichier a l'image
        self.image = pygame.image.load('assets/comet.png')
        # definit un rectangle selon l'image chargee
        self.rect = self.image.get_rect()
        # definit une position de depart de l'image
        self.rect.x = random.randint(20,1000)
        self.rect.y = -random.randint(0,300)
        
    # methode pour detruitre la comete
    def remove(self):
        self.comet_event.all_comets.remove(self)
        # verifit si plus de comete
        if len(self.comet_event.all_comets) == 0 :
            # remettre la barre a 0
            self.comet_event.reset_percent()
            # reapparition des monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
        
    # methode pour faire chuter la comete
    def fall(self):
        self.rect.y += self.velocity
        
        # si elle tombe au sol
        if self.rect.y >= 500:
            # retire la comete du groupe de comete
            self.remove()
            
            # si plus de comete dans le jeu, retour au debut
            if len(self.comet_event.all_comets) == 0:
                # remet le compteur a 0
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
                
                
        # si la comete touche le joueur
        if self.comet_event.game.check_collision(
            self,
            self.comet_event.game.all_players):
            # retire la comete du groupe de comete
            self.remove()
            # retire 20 pv au joueur
            self.comet_event.game.player.damage(20)
            