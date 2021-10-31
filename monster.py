# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:12:59 2021

@author: Matymate
"""

import pygame
import random
import animation

# creation classe pour representer la notion de monstre
# et qui herite de Sprite pour etre un element graphique
#class Monster(pygame.sprite.Sprite):
class Monster(animation.AnimateSprite):  
    
    # constructeur et attributs
    # en lui passant l'objet Game,
    # le nom/type du monstre, sa taille
    # et un offset de la position
    def __init__(self, game, name, size, offset=0):
        # constructeur classe parent
        super().__init__(name, size)
        # attributs Monster
        self.health = 95
        self.max_health = 100
        self.attack = 1
        #self.velocity = random.randint(1,2)
        # memorise le Game dans le Player
        self.game = game
        self.offset = offset
        # definit un fichier a l'image mais retiré car dans AnimateSprite
        # self.image = pygame.image.load('assets/mummy.png')
        # definit un rectangle selon l'image chargee
        self.rect = self.image.get_rect()
        # definit une position de depart de l'image
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        # active l'animation a la creation
        self.start_animation()
        self.score_amount = 10


    # methode pour changer le score de point
    def set_score_amount(self, points):
        self.score_amount = points

    # methode pour choisir vitesse de l'entite courante
    def set_speed(self, speed):
        self.defaul_speed = speed
        self.velocity = random.randint(1, speed)
        

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
            self.velocity = random.randint(1,self.defaul_speed)
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = 540 - self.offset
            
            # ajoute des points au score
            self.game.add_score(self.score_amount)
            
            # si la barre des comete est full
            if self.game.comet_event.is_full():
                # retire le monstre du jeu
                self.game.all_monsters.remove(self)
                   
                # tentative declenchement des cometes
                self.game.comet_event.attempt_fall()
                
                
    # definit une methode pour animer le monstre
    def update_animation(self):
        self.animate(loop=True)


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
      
            
# definir classe Mummy qui herite de Monster
class Mummy(Monster):
    
    # constructeur de Mummy
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_score_amount(20)
  
        
# definir classe Alien qui herite de Monster
class Alien(Monster):
    
    # constructeur de Alien
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)      
        self.health = 250
        self.max_health = 250
        self.attack = 2
        self.set_speed(1)
        self.set_score_amount(50)