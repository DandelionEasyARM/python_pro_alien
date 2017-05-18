# coding: utf-8
import ship as SHIP
import bullet as BULLET


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""

        # 屏幕设置
        self.scrren_width = 1200
        self.scrren_height = 800
        self.bg_color = (255, 255, 255)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_bullet_allowed = 10

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 0, 0, 0

        # 外星人设置
        self.alien_speed = 1
        self.alien_max_num = 10
        #
        self.alien_min_distance_alien = 50
        self.alien_min_distance_wall = 40
        self.alien_min_distance_bottom = 30
        self.alien_min_distance_top = 60

    def set_ship(self, ship, speed, bullet):
        """设置飞船属性"""
        ship.set_move_speed(speed)
        ship.set_bullet_allowed(bullet)
        return True

    def set_ship_default(self, ship):
        """设置默认飞船属性"""
        ship.set_move_speed(self.ship_speed)
        ship.set_bullet_allowed(self.ship_bullet_allowed)
        ship.set_bullets(self.bullet_width, self.bullet_height, self.bullet_color, self.bullet_speed)
        return True

    def set_bullet_info(self, bullet, width, height, speed, color):
        """设置子弹属性"""
        return bullet.setting_info(width, height, speed, color)

    def set_bullet_info_defalut(self, bullet):
        """设置子弹默认属性"""
        return bullet.set_info(self.bullet_width,
                               self.bullet_height,
                               self.bullet_speed,
                               self.bullet_color)

    def cal_alien_num_line(self, alien_distance_alien, alien_distance_wall, scrren):
        """计算一行可以放置多少个外星人"""
        # 屏幕宽度 = （外星人数 - 1）* 外星人间距 + 2 * 外星人到墙距离
        scrren_rect = scrren.get_rect()
        alien_num = int(scrren_rect.width - 2 * alien_distance_wall) / alien_distance_alien + 1
        return alien_num

    def cal_alien_num_line_default(self, scrren):
        """计算一行可以放置多少外星人"""
        scrren_rect = scrren.get_rect()
        return int((scrren_rect.width - 2 * self.alien_min_distance_wall) / self.alien_min_distance_alien + 1)

    def set_alien_info_default(self, aliens, alien_num):
        """设置外星人属性"""
        num = 1
        for alien in aliens:

            rect = alien.get_rect()
            alien_width = alien.get_width()
            alien_height = alien.get_height()
            rect.y = self.alien_min_distance_bottom
            rect.x = self.alien_min_distance_wall + (num - 1) * (alien_width + self.alien_min_distance_alien)
            alien.set_rect(rect)
            num += 1
            print num
            print alien.get_rect()
        return True
