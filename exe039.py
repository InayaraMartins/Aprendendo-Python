# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:25:13 2021

@author: Inayara
"""

'''Exercício Python 39: Faça um programa que leia o ano de 
nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora 
exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que 
passou do prazo.'''

from datetime import date
atual = date.today().year

print('\nGênero: \n[1] Feminino \n[2] Masculino')

sexo = int(input('Digite seu genero:'))

if sexo == 2:
    ano = int(input('Ano de nascimento: '))
    idade = atual-ano
    alistamento = abs(18 -idade)
    print('Quem nasceu em {} tem {} anos em 2021.'.format(ano,idade))
    
    if idade < 18:
        print('Ainda faltam {} anos para o seu alistamento.'. format(alistamento))
        print ('Seu alistamento será em {}.'.format(atual+alistamento))
    elif idade > 18:
        print('Você deveria ter se alistado há {} anos.'.format(alistamento))
        print('Seu alistamento foi em {}.'.format(atual-alistamento))
    else:
        print('Você deve se alistar IMEDIATAMENTE!')

else: 
    print('Você não precisa se alistar!')
    
    
