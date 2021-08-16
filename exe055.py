# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:56:51 2021

@author: Inayara
"""

'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''

maior = 0
menor = 0
for p in range(1,6):
    peso = (float(input('Peso da {}° pessoa: '.format(p))))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('o maior peso lido foi de {} Kg.'.format(maior))
print('o menor peso lido foi de {} Kg.'.format(menor))







