# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:50:11 2021

@author: Matymate
"""
import pygame

# creation classe pour gere le projectile du joueur
# et qui herite de Sprite pour etre une image
class Projectile(pygame.sprite.Sprite):
    
    # constructeur avec un argument player et attributs
    def __init__(self, player):
         # constructeur classe parent
        super().__init__()
        self.velocity = 8
        # memorise le Player auquel appartient le ce Projectile
        self.player = player
        # definit un fichier a l'image
        self.image = pygame.image.load('assets/projectile.png')
        # redimensionne l'image
        self.image = pygame.transform.scale(self.image, (50, 50))
        # definit un rectangle selon l'image chargee
        self.rect = self.image.get_rect()
        # positionne le projectile a la position du player passé en arg
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        # conserve l'image de base et definit
        self.origin_image = self.image
        self.angle = 0
    
    
    # methode pour faire tourner l'image en deplacment
    def rotate(self):
        # tourne l'image de 12°
        self.angle += 1
        # rotation de + angle et scale=1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        # pour eviter saccade, reassigne le centre de l'image
        self.rect = self.image.get_rect(center=self.rect.center)        
    
    
    # methode pour delete le projectile actuel du groupe de projectile
    def remove(self):
        self.player.all_projectiles.remove(self)
    
    
    # methode pour deplacer le projectile
    def move(self):
        # deplacement vers la droite
        self.rect.x += self.velocity
        # appel la rotation de l'image
        self.rotate()

        # verifi si projecile en collision avec un monstre
        # de la liste retournee par 'check_collision's
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprime le projectile
            self.remove()
            # inflige des degats au monstre
            monster.damage(self.player.attack)    
        
        
        # si projectile hors ecran
        if self.rect.x > 1080:
            # delete le projectile dans le groupe du player
            self.player.all_projectiles.remove(self)
            
    