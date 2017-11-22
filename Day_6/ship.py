# -*- coding:UTF-8 -*-
import pygame
from settings import Settings

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') #获取图片对象 pygame.image.load()
        self.rect = self.image.get_rect() #获取对象的外接矩形 get_rect()
        self.screen_rect = screen.get_rect() #获取屏幕的外接矩形

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx #图片外接矩形中心设置与屏幕外接矩形的中心在同一垂直线上 centerx为相应中心点的x坐标
        self.rect.bottom = self.screen_rect.bottom #图片外接矩形下边缘y坐标设置为屏幕底部的y坐标 （相应的 top right left）

        #移动标志
        self.moving_right = False
        self.moving_left = False

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed

        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect) #两个参数：图片对象 图片外接矩形被设置的位置

    def center_ship(self):
        self.center = self.screen_rect.centerx