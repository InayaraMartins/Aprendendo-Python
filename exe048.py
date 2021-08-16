# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:06:46 2021

@author: Inayara
"""

'''Exercício Python 48: Faça um programa que calcule a soma entre todos 
os números IMPARES que são múltiplos de três e que se encontram no intervalo de 
1 até 500.'''

soma = 0
cont =0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1  
print('A soma de todos os {} valores solicitados é {}'. format(cont, soma))