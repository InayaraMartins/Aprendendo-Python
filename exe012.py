# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:56:34 2021

@author: Inayara
"""

'''Faça um algoritimo que leia o preço de um produto e mostre seu novo preço
 com 5% de desconto.'''
 
 
p=float(input('Valor do produto sem desconto: R$ '))
d = p*0.05
np = p-d
print(f'O produto que cutava R${p:.2f}, na promoção com desconto de 5% vai custar R${np:.2f}')