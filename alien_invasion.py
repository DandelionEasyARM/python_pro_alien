#coding: utf-8


import sys
import pygame
from settings import Settings
from ship import Ship


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

#   开始游戏的主循环
    while True:

#         监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

#       每次循环时都重绘屏幕
        scrren.fill(ai_settings.bg_color)
        ship.blitme()

#       让最近绘图的屏幕可见
        pygame.display.flip()


print run_game.__doc__
run_game()


