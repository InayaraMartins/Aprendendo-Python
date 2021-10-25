# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:33:14 2021

@author: Inayara
"""

'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário 
se ele quer mostrar mais alguns termos. O programa encerrará quando ele
 disser que quer mostrar 0 termos.'''
 
print('\nGERADOR DE PA')
print('='*15)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo = termo + r
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos.'.format(total))
        
    