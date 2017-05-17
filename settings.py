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
        self.ship_bullet_allowed = 5

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = 0, 0, 0

    def set_ship(self, ship, speed, bullet):
        ship.set_move_speed(speed)
        ship.set_bullet_allowed(bullet)

    def set_ship_default(self, ship):
        ship.set_move_speed(self.ship_speed)
        ship.set_bullet_allowed(self.ship_bullet_allowed)
        ship.set_bullets(self.bullet_width, self.bullet_height, self.bullet_color, self.bullet_speed)

    def set_bullet_info(self, bullet, width, height, speed, color):
        bullet.setting_info(width, height, speed, color)

    def set_bullet_info_defalut(self, bullet):
        bullet.set_info(self.bullet_width,
                        self.bullet_height,
                        self.bullet_speed,
                        self.bullet_color)
