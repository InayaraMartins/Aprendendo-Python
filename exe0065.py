# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 20:25:20 2021

@author: Inayara
"""

'''Exercício Python 65: Crie um programa que leia vários números inteiros
 pelo teclado. No final da execução, mostre a média entre todos os valores
 e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
 usuário se ele quer ou não continuar a digitar valores.'''
 
 
soma = 0
total = 0
maior = 0
menor = 0

while True:
    n = int(input('Digite um número inteiro: '))
    total = total + 1
    soma = soma + n
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
            
    condicao = input('Deseja continuar: S/N  ').upper()
    if condicao == 'S': 
        continue     
    else:
        break
media = soma/ total
print('Total de números digitados:{}'.format(total))
print('Soma dos valores:{}'.format(soma))
print('Média: {}'.format(media))
print('O maior número foi: {}'.format(maior))
print('O menor número foi: {}'.format(menor))

