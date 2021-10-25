# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:53:16 2021

@author: Inayara
"""

'''Exercício Python 060: Faça um programa que leia um número qualquer e 
mostre o seu fatorial.'''

#usando a função math

'''from math import factorial

num = int(input('Digite um número: '))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num,f))'''




'''num = int(input('Digite um número: '))
f = 1
x = num
print('Calculando {}! = '. format(num), end='')
while x > 0:
    print('{} '.format(x), end ='')
    print('X ' if x > 1 else '=', end ='')
    f = f * x
    x = x - 1
print(' {}'.format(f))'''

f = 1
num = int(input('Digite um número: '))
for i in range(num, 0, -1):
    print('{} '.format(i), end ='')
    print('X ' if i > 1 else '= ', end ='')
    f = f * i
print(f)
    

