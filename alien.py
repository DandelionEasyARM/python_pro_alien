#coding: utf-8


import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, screen):
        """初始化外星人"""
        super(Alien, self).__init__()
        self.__screen = screen

        # 加载外星人图像
        self.__image = pygame.image.load_extended('alien.png')
        self.__rect = self.__image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.__rect.x = self.__rect.width
        self.__rect.y = self.__rect.height
        self.__center = self.__rect.centerx

        # 存储外星人准确的位置
        self.__x = float(self.__rect.x)
        self.__y = float(self.__rect.y)

        self.__speed = 1
        self.__min_distance_alien = 50
        self.__min_distance_wall = 40
        self.__current_distance_alien_left = 0
        self.__current_distance_alien_right = 0
        self.__current_distance_wall_left = 0
        self.__current_distance_wall_right = 0
        self.__current_distance_bottom = 0
        self.__current_distance_top = 0

    def blitme(self):
        """在指定的位置绘制外星人"""
        self.__screen.blit(self.__image, self.__rect)

    def update(self):
        """重写更新函数,根据移动规则改变外星人位置"""
        # self.__y += self.__speed
        # self.__x += self.__speed
        # self.__rect.y = self.__y
        # self.__rect.x = self.__x
        # self.__center = self.__rect.centerx

    def moving(self):
        """移动外星人"""

    def stop(self):
        """停止外星人"""

    def set_move_speed(self, speed):
        """设置移动速度"""
        self.__speed = speed

    def get_scrren(self):
        return self.__screen

    def set_rect(self, rect):
        self.__rect = rect
        return True

    def get_rect(self):
        return self.__rect

    def set_width(self, width):
        self.__rect.x = width
        return True

    def get_width(self):
        return self.__rect.x

    def set_height(self, height):
        self.__rect.y = height
        return True

    def get_height(self):
        return self.__rect.y

    def get_self_center(self):
        return self.__center

    def get_distance_alien(self):
        return self.__min_distance_alien

    def get_distance_wall(self):
        return self.__min_distance_wall




