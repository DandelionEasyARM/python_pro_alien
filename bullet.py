#coding: utf-8


import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对飞船所出的位置设置子弹进行管理的类"""
    def __init__(self, scrren, ship):
        """对飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.__scrren = scrren
        self.__width = ship.get_bullets_width()
        self.__height = ship.get_bullets_height()
        self.__color = ship.get_bullets_color()
        self.__speed = ship.get_bullets_speed()

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.__width, self.__height)
        self.rect.centerx = ship.get_self_center()
        rect = ship.get_rect()
        self.rect.top = rect.top

        # 存储用小数表示的子弹的位置
        self.__y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.__y -= self.__speed
        # 更新表示子弹的rect位置
        self.rect.y = self.__y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.__scrren, self.__color, self.rect)

    def set_info(self, width, height, speed, color):
        """设置子弹基本属性"""
        self.__width = width
        self.__height = height
        self.__color = color
        self.__speed = speed

    def get_width(self):
        """获取宽度"""
        return self.__width

    def get_hight(self):
        """获取高度"""
        return self.__height

    def get_speed(self):
        """获取速度"""
        return self.__speed

    def get_color(self):
        """获取颜色"""
        return self.__color

    def get_rect(self):
        return self.rect


def delete_bullte(bullet, bulltes):
        rect = bullet.get_rect()
        if 0 >= rect.bottom:
            bullet.remove(bulltes)
