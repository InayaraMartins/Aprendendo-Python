# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:48:21 2021

@author: Inayara
"""

'''Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.'''


numero=int(input('Informe um número: '))
n = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Analisando o número {numero}')
print(f'Unidade:{n}')
print(f'Dezena: {d}')
print(f'Centena:{c}')
print(f'Milhar:{m}')

