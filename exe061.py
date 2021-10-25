# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:56:02 2021

@author: Inayara
"""

'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e
 a razão de uma PA, mostrando os 10 primeiros termos da progressão 
 usando a estrutura while.'''
 
print('\nGERADOR DE PA')
print('='*15)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = n
cont = 1
while cont <=10:
    print('{} ->'.format(termo), end='')
    termo = termo + r
    cont = cont + 1
print('FIM')
    
    
'''p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p +(11 - 1)*r
for c in range(p, d , r):
    print('{} -> '.format(c), end=' ')
print('ACABOU!')'''