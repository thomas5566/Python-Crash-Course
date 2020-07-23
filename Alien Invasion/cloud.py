import pygame

class Cloud():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/cloud.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left

    def topitem(self):
        self.screen.blit(self.image, self.rect)


