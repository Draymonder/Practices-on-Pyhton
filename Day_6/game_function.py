# -*- coding:UTF-8 -*-
import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

def check_events(ai_settings, stats, screen, ship, bullets, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没到限制子弹数，就发射一颗子弹"""
    #创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship) #实例化一个子弹类
        bullets.add(new_bullet)

def update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #画子弹（一个一个画）
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #画船
    ship.blitme()

    #画外星人
    aliens.draw(screen)

    #画PLAY按钮
    if not stats.game_active:
        play_button.draw_button()

    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    #检查是否击中外星人
    #若击中，则删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if len(aliens) == 0:
        #删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    #创建一个外星人并计算一行可容纳多少外星人
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    #创建外星人群
    for number_row in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, number_row)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)

def get_number_alien_x(ai_settings, alien_width):
    """计算每行能容纳的外星人个数"""
    available_space_x = ai_settings.width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = ai_settings.height - 3 * alien_height - ship_height
    number_rows = int (available_space_y / (2 * alien_height))
    return number_rows

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #检测外星人与飞船的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    #检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到飞船"""
    if stats.ships_left > 0 :
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

