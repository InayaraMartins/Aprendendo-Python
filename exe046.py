# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:20:16 2021

@author: Inayara
"""

'''Exercício Python 46: Faça um programa que mostre na tela uma 
contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''




import time
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('BUM! BUM! POOOW!!')
    