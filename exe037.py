# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 19:45:09 2021

@author: Inayara
"""

'''Exercício Python 37: Escreva um programa em Python que leia 
um número inteiro qualquer e peça para o usuário escolher qual
 será a base de conversão: 1 para binário, 2 para octal 
 e 3 para hexadecimal.'''
 
n = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('[1] converter para binário.')
print('[2] converter para octal.')
print('[3] converter para hexadecimal.')

escolha =int(input('Sua opção: '))

if escolha == 1:
    binario = (bin(n)[2:])
    print('{} convertido para binario é igual a {}'.format(n, binario))

elif escolha == 2:
    octal =(oct(n)[2:])
    print(('{} convertido para octal é igual a {}'.format(n, octal)))

elif escolha == 3:
    hexa = (hex(n)[2:])
    print(('{} convertido para hexadecimal é igual a {}'.format(n, hexa)))

else:
    print('Essa opção não é válida!')
    