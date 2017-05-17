#coding: utf-8


import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
import bullet as Bullte


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()

    scrren = pygame.display.set_mode((ai_settings.scrren_width, ai_settings.scrren_height))
    pygame.display.set_caption("Alien Invasion")

#   创建一艘飞船
    ship = Ship(scrren)
    ai_settings.set_ship_default(ship)
    # bullets = Group()

#   开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(ship)

        # 每次循环时都重绘屏幕
        # bullets.update()
        gf.redraw_scrren(ai_settings, scrren, ship)


print run_game.__doc__
run_game()


