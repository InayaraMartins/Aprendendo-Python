# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:24:50 2021

@author: Inayara
"""

'''Exercício Python 071: Crie um programa que simule o funcionamento de um 
caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser 
sacado (número inteiro) e o programa vai informar quantas cédulas de cada 
valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''


print('BANCO CEV')

valor = float(input('Que valor você quer sacar? '))

if valor > 50:
    cont50 = valor//50
    valor = valor - (cont50 *50)
    print('Total de {:.0f} cédulas de R$ 50,00.'.format(cont50))

if valor > 20:
    cont20 = valor//20
    valor = valor - (cont20 *20)
    print('Total de {:.0f} cédulas de R$ 20,00.'.format(cont20))

if valor > 10:
    cont10 = valor//10
    valor = valor - (cont10 *10)
    print('Total de {:.0f} cédulas de R$ 10,00.'.format(cont10))

if valor > 1:
    cont1 = valor
    print('Total de {:.0f} cédulas de R$ 1,00.'.format(cont1))
    



    


