#coding: utf-8


import pygame
from pygame.sprite import Sprite
import random as Random


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, screen):
        """初始化外星人"""
        super(Alien, self).__init__()
        self.__screen = screen

        # 加载外星人图像
        self.__image = pygame.image.load_extended('alien.png')
        self.rect = self.__image.get_rect()
        self.__scrren_right = self.__screen.get_width()
        # self.__screen_left = self.__rect.x
        self.__scrren_left = 0
        self.__scrren_top = self.__screen.get_height()
        # self.__screen_bottom = self.__rect.y
        self.__scrren_botoom = 0

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = 0
        self.rect.y = 0
        self.__center = 0

        # 存储外星人准确的位置
        self.__x = float(self.rect.x)
        self.__y = float(self.rect.y)

        direction_temp = Random.randint(0, 1)
        if 0 == direction_temp:
            self.__fleet_direction = 'left'
        else :
            self.__fleet_direction = 'right'
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
        self.__screen.blit(self.__image, self.rect)

    def update(self):
        """重写更新函数,根据移动规则改变外星人位置"""
        # self.__x = self.__rect.x
        # self.__y = self.__rect.y
        # self.__center = self.__rect.centerx

        if (self.rect.x + self.rect.width) >= self.__scrren_right:
            self.__fleet_direction = 'left'
        elif self.rect.x <= self.__scrren_left:
            self.__fleet_direction = 'right'

        if self.__fleet_direction == 'right':
            self.__x += self.__speed
        elif self.__fleet_direction == 'left':
            self.__x -= self.__speed

        self.__y += self.__speed
        self.rect.y = self.__y
        self.rect.x = self.__x
        self.__current_distance_wall_left = self.__x - self.__scrren_left
        self.__current_distance_wall_right = self.__scrren_right - self.__x - self.rect.width
        self.__current_distance_bottom = self.__x - self.__scrren_botoom
        self.__current_distance_top = self.__scrren_top - self.__y - self.rect.height


    def moving(self):
        """移动外星人"""

    def stop(self):
        """停止外星人"""

    def set_move_speed(self, speed):
        """设置移动速度"""
        self.__speed = speed

    def get_scrren(self):
        return self.__screen

    def set_speed(self, speed):
        self.__speed = speed
        return True

    def set_rect(self, rect):
        self.rect = rect
        self.__x = rect.x
        self.__y = rect.y
        return True

    def get_rect(self):
        return self.rect

    def set_x(self, x):
        self.rect.x = x
        return True

    def get_x(self):
        return self.rect.x

    def set_y(self, y):
        self.rect.y = y
        return True

    def get_y(self):
        return self.rect.y

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def get_self_center(self):
        return self.__center

    def get_distance_alien(self):
        return self.__min_distance_alien

    def get_distance_wall(self):
        return self.__min_distance_wall

    def get_distance_wall_left(self):
        return self.__current_distance_wall_left

    def get_distance_wall_right(self):
        return self.__current_distance_alien_right

    def get_distance_wall_bottom(self):
        return self.__current_distance_bottom

    def get_distance_wall_top(self):
        return self.__current_distance_top




