#!/usr/bin/python
# -*- coding: utf-8 -*-

# PARA INICIAR O PACOTE DO PYGAME PRIMEIRO DEVO FAZER:
import pygame
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))  # CRIAÇÃO DE UMA JANELA, ELE INICIALIZA O DISPLAY

    def run(self):

        while True:  # PARA SE MANTER A JANELA ABERTA E NÃO FECHAR DEVO FAZER UM LAÇO INFINITO
            menu = Menu(self.window)
            menu.run()

