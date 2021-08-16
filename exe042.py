# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:41:11 2021

@author: Inayara
"""

'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um TRIANGULO' , end=' ')   
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 and r1 != r3 and r2 != r3 or r1 == r3 and r1 != r2 and r3 != r2 or r2 == r3 and r2 != r1 and r3 != r1:
        print('Triangulo ISÓCELES')
    elif r1 != r2 != r3 != r1:
        print('Triangulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar TRIANGULOS.')