# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:20:08 2021

@author: Inayara
"""

'''
Crie um algoritimo que leia um número e mostre seu dobro, seu triplo e 
sua raiz quadrada
'''
n1 = int(input('Digite um número:  '))
dobro = n1*2
triplo = n1*3
raiz = n1**(1/2)
print(f'Considerando o número {n1}, \nseu dobro é {dobro}, \ntriplo {triplo} e \nsua raíz é {raiz:.2f}')

