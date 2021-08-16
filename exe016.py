# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:35:10 2021

@author: Inayara
"""

'''Crie um programa que leia um número Real qualquer pelo teclado 
e mostre na tela a sua porção Inteira.'''

import math
num=float(input('Digite um número: '))
print(f'O número digitado é {num} e o número inteiro é {math.trunc(num)}')


'''from math import trunc
num=float(input('Digite um número: '))
print(f'O número digitado é {num} e o número inteiro é {trunc(num)}')'''

'''num=float(input('Digite um número: '))
print(f'O número digitado é {num} e o número inteiro é {int(num)}')'''

