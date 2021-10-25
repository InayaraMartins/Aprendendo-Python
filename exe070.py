# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:45:30 2021

@author: Inayara
"""

'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários 
produtos. O programa deverá perguntar se o usuário vai continuar ou não.
 No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
    
total = 0 
totmil = 0
cont = 0
menor = 0
barato = ' '
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if res == 'N':
        break

print('O total da compra foi R$ {:.2f}'.format(total))
print('Temos {} produto custando mais de R$ 1000,00'.format(totmil))
print('O produto mais barato foi {} que custa R$ {}'.format(barato,menor))
