# -*- coding:UTF-8 -*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """初始化外星人并设置其起始位置"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect() #通过图片得到外界矩形对象

        #每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width #改变外接矩形对象的属性
        self.rect.y =  self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果位于屏幕边缘，返回True"""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        """向左或向右移动外星人"""
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
        self.rect.x = self.x