# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 11:46:30 2021

@author: Inayara
"""

'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete 
pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e 
quantas já são maiores.'''


from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input('Digite o {} ano de nascimento: '. format(c)))
    idade = atual - ano
    if idade > 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))