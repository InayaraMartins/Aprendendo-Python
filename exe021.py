# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:09:39 2021

@author: Inayara
"""

''' Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3'''

import pygame
pygame.init()
pygame.mixer.music.load('01 Chapada.MP3')
pygame.mixer.music.play()
pygame.mixer.wait

