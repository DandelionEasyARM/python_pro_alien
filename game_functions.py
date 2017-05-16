#coding: utf-8

import sys
import pygame


def check_event(ship):
    #监视键盘和鼠标事件
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            sys.exit()
        elif pygame.KEYDOWN == event.type:
            if pygame.K_RIGHT == event.key:
                #向右移动飞船
                ship.moving('right')
                ship.update()
            if pygame.K_LEFT == event.key:
                #向左移动飞船
                ship.moving('left')
                ship.update()
        elif pygame.KEYUP == event.type:
            ship.stop()

def update_scrren(ai_settings, scrren, ship):
    """更新屏幕上的图像"""
    # 每次循环时都重绘屏幕
    scrren.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘图的屏幕可见
    pygame.display.flip()
