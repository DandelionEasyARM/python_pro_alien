#coding: utf-8

import sys
import pygame


def check_keyup_event(event, ship):
    """按键释放事件响应"""
    ship.stop()

def check_keydown_event(event, ship):
    """按键按下事件响应"""
    if pygame.K_RIGHT == event.key:
        # 向右移动飞船
        ship.moving('right')
    if pygame.K_LEFT == event.key:
        # 向左移动飞船
        ship.moving('left')

def check_event(ship):
    """检测按键事件"""
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            sys.exit()
        elif pygame.KEYDOWN == event.type:
            check_keydown_event(event, ship)
        elif pygame.KEYUP == event.type:
            check_keyup_event(event, ship)

def update_scrren(ai_settings, scrren, ship):
    """更新屏幕上的图像"""
    # 每次循环时都重绘屏幕
    scrren.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘图的屏幕可见
    pygame.display.flip()
