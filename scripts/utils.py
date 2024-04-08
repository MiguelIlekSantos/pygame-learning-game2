import pygame
import os

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    imgSurf = pygame.image.load(BASE_IMG_PATH + path).convert()
    imgSurf.set_colorkey((0,0,0))
    return imgSurf    

def load_images(path):
    tiles = []
    for tileName in os.listdir(BASE_IMG_PATH + path):
        tiles.append(load_image(path + '/' + tileName))
    return tiles


class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True


    def img(self):
        return self.images[int(self.frame / self.img_duration)]




