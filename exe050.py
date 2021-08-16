# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:18:38 2021

@author: Inayara
"""

'''Exercício Python 50: Desenvolva um programa que leia seis números 
inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
cont = 0
for c in range(1,7):
    n= int(input('Digite o {}° número inteiro: '.format(c)))
    if n % 2 == 0:
        soma = soma + n # soma += n
        cont = cont + 1 # cont += 1
print('Você informou {} números  PARES e a soma é {}.'. format(cont, soma))
        
 
        
        
   