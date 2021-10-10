# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:09:08 2021

@author: Inayara
"""

'''Exercício Python 57: Faça um programa que leia o sexo de 
uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
errado, peça a digitação novamente até ter um valor correto.'''



sexo = str(input('Informe seu sexo: [F/M] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo:[F/M] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))