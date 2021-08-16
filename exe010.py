# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:11:13 2021

@author: Inayara
"""

'''Crei um programa que leia quanto de dinheiro a pessoa tem na carteira e mostre 
quantos dólares ela pode comprar considere RSS 1,00 = R$ 3,27 reais'''

real=float(input('Quanto dinheiro em reais você tem na sua carteira? R$'))
dolar = real/5.55
euro = real/6.64
libra = real/7.73
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
print(f'Com R${real:.2f} você pode comprar €{euro:.2f}')
print(f'Com R${real:.2f} você pode comprar £{libra:.2f}')