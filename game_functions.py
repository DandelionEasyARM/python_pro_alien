#coding: utf-8

import sys
import pygame
import bullet as BULLET
from bullet import *


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
    if pygame.K_SPACE == event.key:
        # 空格键，飞船开火
        ship.fire_bullets()

    if pygame.K_ESCAPE == event.key:
        sys.exit()


def check_event(ship):
    """检测按键事件"""
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            sys.exit()
        elif pygame.KEYDOWN == event.type:
            check_keydown_event(event, ship)
        elif pygame.KEYUP == event.type:
            check_keyup_event(event, ship)


def redraw_bullet(bullets):
    bullets.update()
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.copy():
        BULLET.delete_bullte(bullet, bullets)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    print len(bullets)

def redraw_scrren(ai_settings, scrren, ship):
    """更新屏幕上的图像"""
    # 每次循环时都重绘屏幕
    scrren.fill(ai_settings.bg_color)

    bullets = ship.get_bullets()
    redraw_bullet(bullets)

    ship.blitme()
    # 让最近绘图的屏幕可见
    pygame.display.flip()
    ship.update()
    bullets.update()





