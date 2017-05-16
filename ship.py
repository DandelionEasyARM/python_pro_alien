# coding: utf-8

import pygame


class Ship():

    def __init__(self, scrren):
        """初始化飞船并设置其初始位置"""
        self.scrren = scrren
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.scrren_rect = scrren.get_rect()

#       将每艘飞船防止在屏幕底部中央
        self.rect.centerx = self.scrren_rect.centerx
        self.rect.bottom = self.scrren_rect.bottom

    def blitme(self):
        """在指定位置放置飞船"""
        self.scrren.blit(self.image, self.rect)

