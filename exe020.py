# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:35:12 2021

@author: Inayara
"""

'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de 
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos 
e mostre a ordem sorteada.'''


import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

