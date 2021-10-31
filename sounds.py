# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:23:14 2021

@author: Matymate
"""

import pygame

# Classe pour gerer les sons
class SoundManager:
    
    def __init__(self):
        # dictionnaire des effets sonores
        self.sounds = {
            'click': pygame.mixer.Sound("assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'meteorite': pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("assets/sounds/tir.ogg"),
        }
        
    
    # methode pour jouer un son en lui passant son nom
    def play(self, name):
        self.sounds[name].play()
        