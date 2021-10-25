# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:44:06 2021

@author: Inayara
"""

'''Exercício Python 67: Faça um programa que mostre a tabuada de vários
 números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.'''
 
 
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('='*30)
    if tabuada < 0:
        print('Encerrando tabuada...')
        break
    else:
        for i in range(0,11,1):
            print('{} X {} = {}'.format(tabuada,i,tabuada*i))
        
        
 