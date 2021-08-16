# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:56:37 2021

@author: Inayara
"""

'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um
 número que o usuário escolher, só que agora utilizando um laço for.'''
 
n=int(input('Digite um número:  '))
for j in range(1,11):
    print('{} x {:2} = {}'.format(n, j, n*j))
    