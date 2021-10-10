# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 12:00:35 2021

@author: Inayara
"""

'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o 
computador vai “pensar” em um número entre 0 e 10. Só que 
agora o jogador vai tentar adivinhar até acertar, mostrando 
no final quantos palpites foram necessários para vencer.'''

import random
import time
cont = 1
computador= random.randint(0,10)
print('Sou seu computador...')
time.sleep(1)
print('Acabei de pensar em um número de 0 a 10.')
time.sleep(1)
print('Será que você consegue advinhar qual é?')
time.sleep(1)
palpite = int(input('Qual é seu palpite? '))
while palpite != computador:
    cont = cont + 1
    if computador > palpite:
        print('O número é maior...')
    elif computador < palpite:
        print('O número é menor...')
    palpite = int(input('Tente mais uma vez: '))
if palpite == computador:
    print('Você acertou com {} tentativas. Parabéns!'.format(cont))
    
   