#coding: utf-8


# import sys
import pygame
from settings import *
from ship import Ship
# from alien import Alien
import game_functions as gf
from pygame.sprite import Group
import time
# import bullet as Bullte


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()

    ai_settings = Settings()
    game_state = GameState(ai_settings)
    game_state.game_state = 'running'
    scrren = pygame.display.set_mode((ai_settings.scrren_width, ai_settings.scrren_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(scrren)
    ai_settings.set_ship_default(ship)

    # 创建外星人
    aliens = Group()
    alien_num = ai_settings.cal_alien_num_line_default(scrren)
    gf.creat_fleet_alien(scrren, game_state, aliens, alien_num)
    ai_settings.set_alien_info_default(aliens, alien_num)

#   开始游戏的主循环
    while True:
        # 0.监视键盘和鼠标事件
        gf.check_event(ship)

        # 1.更新飞船数据
        ship.update()

        # 2.更新外星人数据
        aliens.update()

        # 3.命中外星人处理
        gf.alien_short(scrren, game_state, aliens, ship, ai_settings)

        # 4.外星人过线和飞船碰撞处理
        gf.shiphit_alienoverline(scrren, game_state, ship, aliens)

        # 5.重绘屏幕
        gf.redraw_scrren(ai_settings.bg_color, scrren, ship, aliens)

        # time.sleep(1)

print run_game.__doc__
run_game()


