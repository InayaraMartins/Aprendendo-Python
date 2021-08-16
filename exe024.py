# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:34:55 2021

@author: Inayara
"""

'''Crie um programa que leia o nome de uma cidade diga se ela 
começa ou não com o nome “SANTO”.'''

nome=str(input('Em que cidade você nasceu? ')).strip()
print(nome[:5].upper() =='SANTO')
