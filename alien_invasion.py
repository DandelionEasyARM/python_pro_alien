#coding: utf-8


import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()

    scrren = pygame.display.set_mode((ai_settings.scrren_width, ai_settings.scrren_height))
    pygame.display.set_caption("Alien Invasion")

#   设置背景颜色
    bg_color = (230, 230, 230)

#   创建一艘飞船
    ship = Ship(scrren)
    ship.set_move_speed(5)

#   开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(ship)

        # 每次循环时都重绘屏幕
        gf.update_scrren(ai_settings, scrren, ship)
        ship.update()

print run_game.__doc__
run_game()


