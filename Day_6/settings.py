# -*- coding:UTF-8 -*-
class Settings():
    """存储游戏所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.width = 1200
        self.height = 800
        self.bg_color = (230, 230, 230)

        #飞船速度
        self.ship_speed = 4.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3


        #外星人设置
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        #fleet_direction = 1 表示向右,fleet_direction = -1表示向左
        self.fleet_direction = 1