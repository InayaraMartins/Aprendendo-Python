# -*- coding: utf-8 -*-
"""
Created on Thu May 13 17:29:34 2021

@author: Inayara
"""

'''Exercício Python 30: Crie um programa que leia um número 
inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

numero = int(input('Me diga um número qualquer: '))

if (numero%2) == 0:
    print('O número {} é Par'.format(numero))
else:
    print('O número {} é Ímpar'.format(numero))