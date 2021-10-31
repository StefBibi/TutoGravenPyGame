# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:00:22 2021

@author: Matymate
"""
import pygame

from comet import Comet


# creation classe pour gerer l'evenement des cometes
class CometFallEvent():
    
    # constructeur
    def __init__(self, game):
        self.game = game
        # attribut compteur
        self.percent = 0
        # attribut pour gerer l'increment moins rapide du compteur
        self.percent_speed = 20
        # creer un groupe de Sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()
        # attribut pour gerer l'activation des evenements
        self.fall_mode = False
        
    # methode pour ajouter incrementer le compteur
    def add_percent(self):
        self.percent += self.percent_speed / 100
        
    # methode pour maj une barre s'affichant en bas de l'ecran
    def update_bar(self, surface):
        # incremente le compteur (1 / frame)
        self.add_percent()
        
        # barre noire en arriere plan
        pygame.draw.rect(surface, (0,0,0),[
            0, # position sur axe des x
            surface.get_height()-30, # position sur axe des y
            surface.get_width(), # longueur de la barre
            10 # hauteur de la barre
        ])
        
        # barre rouge pour le compteur
        pygame.draw.rect(surface, (187,11,11),[
            0, # position sur axe des x
            surface.get_height()-30, # position sur axe des y
            (surface.get_width()/ 100) * self.percent, # longueur de la barre
            10 # hauteur de la barre
        ])
        
    #☻ methode pour verifier si barre comete full
    def is_full(self):
        return self.percent >= 100
    
    # methode pour raz le compteur des cometes
    def reset_percent(self):
        self.percent = 0
    
    # methode pour creer 10 cometes et ajouter au groupe des cometes
    def comet_fall(self):
        for i in range(1, 10):
            self.all_comets.add(Comet(self))

    # methode pour declencher les cometes
    def attempt_fall(self):
        # si barre comete pleine et plus de monstre
        if self.is_full() and len(self.game.all_monsters)==0:
            # declenche la pluie de comete
            self.comet_fall()
            # pour gerer l'activation des evenements
            self.fall_mode = True
