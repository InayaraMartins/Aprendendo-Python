# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:43:55 2021

@author: Inayara
"""

''' Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = (l*a)
tinta = area/2
print(f'Sua parede tem a dimensão de {l} X {a} e sua área é de {area} m2')
print(f'Para pintar essa parede, você precisará de {tinta} L de tinta')

