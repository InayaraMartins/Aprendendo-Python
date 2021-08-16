# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:27:22 2021

@author: Inayara
"""

'''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''


nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... ')
print(f'Seu nome em maiúsculo é: {nome.upper()}')
print(f'Seu nome em minúsculo é: {nome.lower()}')
#print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
espaço= (len(nome)-nome.count(' '))
print(f'Seu nome tem {espaço} letras')
divisão = nome.split()
print(f'Seu primeiro nome é {divisão[0]} e tem {len(divisão[0])} letras')