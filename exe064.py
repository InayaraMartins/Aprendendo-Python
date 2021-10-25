# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 20:00:58 2021

@author: Inayara
"""

'''Exercício Python 64: Crie um programa que leia vários números inteiros
 pelo teclado. O programa só vai parar quando o usuário digitar o valor 
 999, que é a condição de parada. No final, mostre quantos números foram 
 digitados e qual foi a soma entre eles (desconsiderando o flag).'''
 
 
soma = 0
total = 0
while True:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    if n == 999:
        break
    else:
        total = (total +1)
        soma = soma + n
print('Total de números digitados:{}'.format(total))
print('Soma dos valores:{}'.format(soma))
