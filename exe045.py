# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 21:42:29 2021

@author: Inayara
"""

'''Exercício Python 45: Crie um programa que faça o computador 
jogar Jokenpô com você.'''


import random
import time
print('''SUAS OPÇÕES: \n
         [0] PEDRA
         [1] PAPEL
         [2] TESOURA''')
         
jogada = int(input('Qual é a sua jogada? '))

if jogada == 0:
    y='PEDRA'
elif jogada == 1:
    y ='PAPEL'
elif jogada == 2:
    y = 'TESOURA'

x= random.randint(0,2)

if x == 0:
    n='PEDRA'
elif x == 1:
    n ='PAPEL'
elif x == 2:
    n = 'TESOURA'
    
    
print('JO')
time.sleep(1)
print('KE')
time.sleep(1)
print('PO!')
time.sleep(1)
         
print('=-'*20)
print('Computador jogou {}.'.format(n))
print('Você jogou {}'.format(y))
print('=-'*20)

if x == jogada:
    print('EMPATE!!!')
elif (x == 0 and jogada == 2) or (x == 1 and jogada == 0) or (x == 2 and jogada == 1 ):
    print("você PERDEU!!!")
else:
    print('VOCÊ GANHOU!!!!!!')


