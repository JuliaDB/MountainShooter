#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Const import *        # ASTERISCO PUXA TUDO DO CONST


class Menu:
    def __init__(self, window):
        self.window = window
        # COMO CARREGAR UMA IMAGEM NO MENU (BACKGROUND)
        self.surf = pygame.image.load('asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = MENU_OPTION

    def run(self, ):
        pygame.mixer_music.load('./asset/Musica.mp3')  # CARREGA A MÚSICA
        pygame.mixer_music.play(-1)  # TOCA A MÚSICA SEM PARAR EM LOOP (-1 = loop infinito)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_RED, ((580 / 2), 70))
            self.menu_text(50, "Shooter", COLOR_RED, ((580 / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == self.menu_option[i]:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((580 / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_GRAY, ((580 / 2), 200 + 25 * i))

            pygame.display.flip()

            # CHECK FOR ALL EVENTS (cheque por todos os eventos)
            for event in pygame.event.get():  # IF THE EVENT IS QUIT (se o evento for de fechar a janela)
                if event.type == pygame.QUIT:
                    pygame.quit()  # FINALIZA O PYGAME (close window)
                    quit()  # FINALIZA O PROGRAMA
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # MOVIMENTO DE SETAS PRA BAIXO
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
