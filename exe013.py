# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:12:02 2021

@author: Inayara
"""

'''Faça um algoritmo que leia o salário de um funcionário e
 mostre seu novo salário, com 15% de aumento.'''
 
s=float(input('Qual é seu salário atual? '))
a= s + (s*(15/100))
print(f'Um funcionário que recebia R${s:.2f}, com aumento de 15%, passa a receber R${a:.2f}')