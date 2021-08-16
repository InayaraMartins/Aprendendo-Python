# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:49:07 2021

@author: Inayara
"""

'''Crie um programa que leia o nome de uma pessoa e diga se 
ela tem “SILVA” no nome.'''


nome=str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
                                      

#nome=str(input('Qual é seu nome completo? ')).strip().upper()
#print('Seu nome tem Silva?{}'.format('SILVA' in nome))


#print(f'Seu nome é {"SILVA" in nome}') 
#print(f"Seu nome é {'SILVA' in nome}")