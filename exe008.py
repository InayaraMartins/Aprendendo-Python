# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:15:10 2021

@author: Inayara
"""

'''Escreva um programa que leia um valor em metros e o 
exiba convertido em centímetro e milímetro''' 


valor=float(input('Valor em metros:  '))
cm=valor*100
mm=valor*1000
print('    ')
print(f'{valor} metros, equivale a {cm} cm ou a {mm} mm')