# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:56:58 2021

@author: Inayara
"""

'''Exercício Python 36: Escreva um programa para aprovar o 
empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador 
e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então
 o empréstimo será negado.'''
 
 
valorcasa = float(input('Digite o valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
meses= anos*12

prestação = valorcasa/meses

negado = (30/100) * salário

print('Para pagar uma casa no valor de {:.2f} em {} anos a presatação será de {:.2f}'.format(valorcasa, anos, prestação))

if prestação > negado:
    print('Empréstimo NEGADO!')

else:
    print('Emprestimo pode ser CONCEDIDO!')