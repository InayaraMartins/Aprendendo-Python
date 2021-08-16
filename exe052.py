# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:50:48 2021

@author: Inayara
"""

'''Exercício Python 52: Faça um programa que leia um número inteiro e 
diga se ele é ou não um número primo.'''


num = int(input('Digite um número: '))
tot = 0 #variável com valor inicializável 
for c in range(1, num + 1): #vai do número 1 até o número escolhido pelo usuario n+1 pq no python sempre vai um numero antes
    if num % c == 0:
        print('\033[1;33m', end='')
        tot = tot + 1
    else:
        print('\033[1;31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes!'.format(num,tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
    
        
   
    