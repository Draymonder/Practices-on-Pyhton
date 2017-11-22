# -*- coding:UTF-8 -*-
import pygame

class Button():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/play.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 1.5*self.screen_rect.centery
    def draw_button(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect) #两个参数：图片对象 图片外接矩形被设置的位置



