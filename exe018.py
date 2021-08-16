# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:55:11 2021

@author: Inayara
"""

''' Faça um programa que leia um ângulo qualquer e mostre na tela o 
valor do seno, cosseno e tangente desse ângulo.'''

import math
angulo=float(input('Valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O valor do seno é {seno:.2f}, do cosseno é {cos:.2f} e da tangente é {tan:.2f}')
