# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:01:52 2021

@author: Matymate
"""

import pygame

# creation classe pour ferer les animations
# et qui herite de Sprite pour etre un element graphique
class AnimateSprite(pygame.sprite.Sprite):

    # constructeur et argument pour savoir a quel
    # sprite s'applique l'animation
    # et sa taille en option
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        # definit un fichier a l'image
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        # redimensionne l'image a la taille demandée
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # pour commencer l'animation a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False


    # definir une methode pour activer l'animation
    def start_animation(self):
        self.animation = True
        
        
    # definir une methode pour animer le Sprite
    def animate(self, loop=False):
        # verifier que l'animation est activée
        if self.animation:  
            # passer a l'image suivante
            self.current_image += 1
            # verifier si image courante est la derniere de la liste des images
            if self.current_image >= len(self.images):
                # raz de l'image
                self.current_image = 0
                
                # verifier si animation pas en boucle
                if loop is False:
                    self.animation = False
                
            # modifie l'image par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# definit une fonction pour charger les images d'un Sprite
def load_animation_images(sprite_name):
    
    # charger les 24 images adequat au sprite
    images = []
    # recupere le chemin du dossier adequat au sprite
    path= f"assets/{sprite_name}/{sprite_name}"

    # boucle pour sur chaque image du dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        # ajoute l'image dans la liste
        images.append(pygame.image.load(image_path))

    # renvoi la liste
    return images


# definit un dictionnaire contenant les images chargées de cahque Sprite
# mummy -> [...mummy1.png, mummy2.png,  ...]
# player -> [...player1.png, player2.png,  ...]
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
    }