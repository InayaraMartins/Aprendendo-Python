# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:00:18 2021

@author: Inayara
"""

"""Exercício Python 31: Desenvolva um programa que pergunte a 
distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta
 viagens mais longas."""

'''viagem =float(input('Qual a distância da sua viagem: '))
print('Você esta preste a começar uma viagem de {:.1f} Km.'.format(viagem))

if viagem <= 200:
    print('E o preço da sua passagem será de: R$ {:.2f}'.format(viagem * 0.50))
else: 
    print('E o preço da sua passagem será de: R$ {:.2f}'.format(viagem * 0.45))'''

'''viagem =float(input('Qual a distância da sua viagem: '))
print('Você esta preste a começar uma viagem de {:.1f} Km.'.format(viagem))

if viagem <=200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('E o preço da sua passagem será de: R$ {:.2f}'.format(preço))'''

viagem =float(input('Qual a distância da sua viagem: '))
print('Você esta preste a começar uma viagem de {:.1f} Km.'.format(viagem))
preço= viagem * 0.50 if viagem <=200 else viagem * 0.45
print('E o preço da sua passagem será de: R$ {:.2f}'.format(preço))