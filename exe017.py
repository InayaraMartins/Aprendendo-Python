# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:35:07 2021

@author: Inayara
"""

'''Faça um programa que leia o comprimento do cateto oposto e 
do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''


import math
cop=float(input('Comprimento do cateto oposto: '))
caj=float(input('Comprimento do cateto adjacente: '))
print(f'O comprimento da hipotenusa é {math.hypot(cop , caj):.2f}')

'''OBS cálculo da hipotenusa por fórmula: 
    Hipotenusa2 = Cateto oposto2 + Cateto adjacente2
    (cop ** 2 + caj ** 2)**(1/2)'''
