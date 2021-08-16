# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:11:15 2021

@author: Inayara
"""

'''xercício Python 28: Escreva um programa que faça o computador
 “pensar” em um número inteiro entre 0 e 5 e peça para o usuário 
 tentar descobrir qual foi o número escolhido pelo computador. 
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
 
 
import random
import time
computador = random.randint(0, 5)  #faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador =int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
time.sleep(3)
if jogador == computador:
    print('Parabéns!!! Você conseguiu me vencer!')
else:
    print('GANHEI!!! Você pensou no número {} e eu pensei no número {}'.format(jogador, computador))
    