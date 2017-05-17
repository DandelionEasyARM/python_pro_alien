# coding: utf-8

import pygame
import bullet as BULLET
from bullet import *
from pygame.sprite import Group

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
        self.__speed_factor = 1


        # 将每艘飞船防止在屏幕底部中央
        self.rect.centerx = (self.scrren_rect.right + self.scrren_rect.left) / 2
        self.rect.bottom = self.scrren_rect.bottom
        self.self_center = self.rect.centerx

        # 设置对应的子弹
        self.bullet_speed = 1
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = 0, 0, 0

        self.__bullets = Group()
        self.__bullet_allowed = 3

    def blitme(self):
        """在指定位置放置飞船"""
        self.scrren.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if True == self.__moving_riht and self.rect.right < self.scrren_rect.right:
            self.self_center += self.__speed_factor

        if True == self.__moving_left and self.rect.left > self.scrren_rect.left:
            self.self_center -= self.__speed_factor

        self.rect.centerx = self.self_center

    def moving(self, direction):
        """移动飞船"""
        if 'left' == direction:
            self.__moving_left = True
        elif 'right' == direction:
            self.__moving_riht = True
        self.update()

    def stop(self):
        """停止移动,将移动标志位都设置为FALSE"""
        self.__moving_left = False
        self.__moving_riht = False

    def set_move_speed(self, speed):
        """设置飞船移动速度"""
        self.__speed_factor = float(speed)

    def get_bullet_allowed(self):
        return self.__bullet_allowed

    def set_bullet_allowed(self, bullet_allowed):
        self.__bullet_allowed = bullet_allowed

    def get_bullets(self):
        return self.__bullets

    def fire_bullets(self):
        # 限定子弹数量
        if self.__bullet_allowed > len(self.__bullets):
            new_bullet = Bullet(self.scrren, self)
            new_bullet.set_info(self.bullet_width,
                                self.bullet_height,
                                self.bullet_speed,
                                self.bullet_color)
            self.__bullets.add(new_bullet)
