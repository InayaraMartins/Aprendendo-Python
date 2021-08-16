# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:45:41 2021

@author: Inayara
"""

'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a
 razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
 
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p +(11 - 1)*r
for c in range(p, d , r):
    print('{} -> '.format(c), end=' ')
print('ACABOU!')