#coding: utf-8

import sys
import pygame
import bullet as BULLET
from bullet import *
from alien import *
from time import sleep

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


def redraw_ship(ship):
    # 重绘飞船
    ship.blitme()


def redraw_bullet(bullets):
    # 在飞船和外星人后面重绘所有子弹
    bullets.update()
    for bullet in bullets.copy():
        BULLET.delete_bullte(bullet, bullets)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # print len(bullets)


def redraw_alien(aliens):
    for alien in aliens:
        alien.update()
        alien.blitme()


def redraw_scrren(bg_color, scrren, ship, aliens):
    """更新屏幕上的图像"""
    # 1.重刷背景
    scrren.fill(bg_color)

    # 2.重绘飞船
    redraw_ship(ship)

    # 3.重绘子弹
    redraw_bullet(ship.get_bullets())

    # 4.重绘外星人
    redraw_alien(aliens)

    # 让最近绘图的屏幕可见
    pygame.display.flip()


def creat_fleet_alien(screen, game_state, aliens, aliens_num):
    """创建一群外星人"""
    for row in range(aliens_num['row_num']):
        for alien in range(aliens_num['list_num']):
            alien = Alien(screen)
            aliens.add(alien)


def alien_short(scrren, gamge_state, aliens, ship, ai_settings):
    """判断子弹是否命中外星人"""
    bullets = ship.get_bullets()
    # 求子弹和外星人交集
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)

    # 外星人都被消灭时重新创建外星人
    if 0 == len(aliens):
        bullets.empty()
        alien_num = ai_settings.cal_alien_num_line_default(scrren)
        creat_fleet_alien(scrren, aliens, alien_num)
        ai_settings.set_alien_info_default(aliens, alien_num)
    # print collisions


def shiphit_alienoverline(scrren, game_state, ship, aliens):
    """外星人和飞船碰撞和过线处理"""

    # for alien in aliens:
    #     # 任意一个外星人过线
    #     if 0 == alien.get_distance_wall_top():
    #         game_state.game_state = 'stop'

    if pygame.sprite.spritecollideany(ship, aliens):
        game_state.game_state = 'stop'

    if 'stop' == game_state.game_state:
        if 0 == game_state.ships_left:
            game_state.game_active = False
        if game_state.game_active is True:
            bullets = ship.get_bullets()
            bullets.empty()
            aliens.empty()
            sleep(5)
            game_state.ships_left -= 1
            aliens_num = game_state.ai_settings.cal_alien_num_line_default(scrren)
            creat_fleet_alien(scrren, game_state, aliens, aliens_num)
            game_state.ai_settings.set_alien_info_default(aliens, aliens_num)
            ship.center_ship()
            game_state.game_state = 'running'

        else:
            sleep(5)
            sys.exit()


