# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:59:34 2021

@author: Inayara
"""

"""Exercício Python 35: Desenvolva um programa que leia o comprimento de três
 retas e diga ao usuário se elas podem ou não formar um triângulo."""
 
 
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar TRIANGULOS.') 
else:
    print('Os segmentos acima NÃO PODEM formar TRIANGULOS.')
    