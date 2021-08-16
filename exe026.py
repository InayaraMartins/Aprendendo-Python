# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:44:47 2021

@author: Inayara
"""

'''Faça um programa que leia uma frase pelo teclado e mostre 
quantas vezes aparece a letra “A”, em que posição ela aparece
 a primeira vez e em que posição ela aparece a última vez.'''
 
nome=str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} na frase.'.format(nome.count("A"))) 
print('A primeira letra A apareceu na posição {}'.format(nome.find("A")+1)) 
print('A ultima letra A apareceu na posição {}'.format(nome.rfind("A")+1))
