# coding: utf-8

import pygame


class Ship():

    def __init__(self, scrren):
        """初始化飞船并设置其初始位置"""
        self.scrren = scrren
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.scrren_rect = scrren.get_rect()
        # 持续移动标志
        self.__moving_riht = False
        self.__moving_left = False
        self.speed_factor = 1

        # 将每艘飞船防止在屏幕底部中央
        self.rect.centerx = (self.scrren_rect.right + self.scrren_rect.left) / 2
        self.rect.bottom = self.scrren_rect.bottom
        self.self_center = self.rect.centerx


    def blitme(self):
        """在指定位置放置飞船"""
        self.scrren.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""

        if True == self.__moving_riht and self.rect.right < self.scrren_rect.right:
            self.self_center += self.speed_factor

        if True == self.__moving_left and self.rect.left > self.scrren_rect.left:
            self.self_center -= self.speed_factor

        self.rect.centerx = self.self_center

    def moving(self, direction):
        if 'left' == direction:
            self.__moving_left = True
        elif 'right' == direction:
            self.__moving_riht = True

    def stop(self):
        """停止移动,将移动标志位都设置为FALSE"""
        self.__moving_left = False
        self.__moving_riht = False

    def set_move_speed(self, speed):
        """设置飞船移动速度"""
        self.speed_factor = float(speed)
