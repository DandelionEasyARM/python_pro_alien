# coding: utf-8

import pygame
import bullet as BULLET
from bullet import *
from pygame.sprite import Group

class Ship():
    def __init__(self, scrren):
        """初始化飞船并设置其初始位置"""
        self.__scrren = scrren
        # 通过配置文件加载图像
        # ship_file_object = open('ship_image_name.txt', 'r')
        # image_name =ship_file_object.readlines(0)
        # print type(image_name)
        # print image_name[0]
        # image_name_ex = image_name[0]
        # self.__image = pygame.image.load(image_name_ex)
        # ship_file_object.close()
        self.__image = pygame.image.load_extended('ship.png')
        self.__rect = self.__image.get_rect()
        self.__scrren_rect = scrren.get_rect()

        # 持续移动标志
        self.__moving_riht = False
        self.__moving_left = False
        self.__speed_factor = 1

        # 将每艘飞船防止在屏幕底部中央
        self.__rect.centerx = (self.__scrren_rect.right + self.__scrren_rect.left) / 2
        self.__rect.bottom = self.__scrren_rect.bottom
        self.__self_center = self.__rect.centerx

        # 设置对应的子弹
        self.__bullet_speed = 1
        self.__bullet_width = 3
        self.__bullet_height = 10
        self.__bullet_color = 0, 0, 0

        self.__bullets = Group()
        self.__bullet_allowed = 3

    def blitme(self):
        """在指定位置放置飞船"""
        self.__scrren.blit(self.__image, self.__rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if (True is self.__moving_riht) and self.__rect.right < self.__scrren_rect.right:
            self.__self_center += self.__speed_factor

        if (True is self.__moving_left) and self.__rect.left > self.__scrren_rect.left:
            self.__self_center -= self.__speed_factor

        self.__rect.centerx = self.__self_center

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

    def get_scrren(self):
        return self.__scrren

    def get_rect(self):
        return self.__rect

    def get_self_center(self):
        return self.__self_center

    def get_bullet_allowed(self):
        return self.__bullet_allowed

    def set_bullet_allowed(self, bullet_allowed):
        self.__bullet_allowed = bullet_allowed

    def get_bullets(self):
        return self.__bullets

    def get_bullets_width(self):
        return self.__bullet_width

    def get_bullets_height(self):
        return self.__bullet_height

    def get_bullets_color(self):
        return self.__bullet_color

    def get_bullets_speed(self):
        return self.__bullet_speed

    def get_bullets_allowed(self):
        return self.__bullet_allowed

    def set_bullets(self, width, height, color, speed):
        self.__bullet_width = width
        self.__bullet_height = height
        self.__bullet_color = color
        self.__bullet_speed = speed

    def fire_bullets(self):
        # 限定子弹数量
        if self.__bullet_allowed > len(self.__bullets):
            new_bullet = Bullet(self.__scrren, self)
            new_bullet.set_info(self.__bullet_width,
                                self.__bullet_height,
                                self.__bullet_speed,
                                self.__bullet_color)
            new_bullet = Bullet(self.__scrren, self)
            self.__bullets.add(new_bullet)

