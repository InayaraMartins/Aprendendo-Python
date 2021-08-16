# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:20:53 2021

@author: Inayara
"""

''' Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.'''
 
nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}.'.format(lista[0]))
#print('Seu ultimo nome é {}.'.format(lista[-1]))
n= len(lista)-1
print('Seu último nome é {}.'.format(lista[n]))
