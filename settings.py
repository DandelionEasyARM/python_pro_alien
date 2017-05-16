# coding: utf-8


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""

#       屏幕设置
        self.scrren_width = 1200
        self.scrren_height = 800
        self.bg_color = (100, 100, 100)

    def set_ship(self, ship, speed):
        ship.set_move_speed(speed)

class Setting_Ship():
    """飞船通用设置集合"""

