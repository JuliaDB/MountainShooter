#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import MENU_OPTION, COLOR_GRAY, COLOR_YELLOW, COLOR_RED, WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/Menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.selected_option = 0

    def run(self):
        pygame.mixer_music.load('./asset/Musica.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_RED, (WIN_WIDTH / 2, 70))
            self.menu_text(50, "Shooter", COLOR_RED, (WIN_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION)):
                if i == self.selected_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_GRAY, (WIN_WIDTH / 2, 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.selected_option < len(MENU_OPTION) - 1:
                            self.selected_option += 1
                        else:
                            self.selected_option = 0
                    if event.key == pygame.K_UP:
                        if self.selected_option > 0:
                            self.selected_option -= 1
                        else:
                            self.selected_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[self.selected_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
