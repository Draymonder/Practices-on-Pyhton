# -*- coding:UTF-8 -*-
import pygame

import sys
from settings import Settings 
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
import  game_function as gf


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    pygame.display.set_caption("Alien Invasion")
    #创建PLAY按钮
    play_button = Button(screen)
    #创建一个存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    #创建一艘飞船
    ship = Ship(ai_settings, screen) #实例化
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标的事件
        gf.check_events(ai_settings, stats, screen, ship, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button)

run_game()