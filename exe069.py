# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 08:52:19 2021

@author: Inayara
"""

'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias 
pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
    

cont_18 = 0
cont_homem = 0
cont_F_20 = 0

while True:    
    print('-'*20)       
    print('CADASTRO DE PESSOAS') 
    print('-'*20)   
    
    idade = int(input('Idade: ')) 
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        
    if idade > 18:
        cont_18 = cont_18 + 1
    
    if sexo == 'M':
        cont_homem = cont_homem + 1
   
    if sexo == 'F' and idade < 20: 
        cont_F_20 = cont_F_20 + 1
        
    continuar = ' '
    while continuar not in 'SN':    
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        
    if continuar == 'N':
        print('Encerrando cadastros!')
        break

print('{} pessoas tem mais de 18 anos.'.format(cont_18))
print('{} homens foram cadastrados'.format(cont_homem))
print('{} mulheres tem menos de 20 anos.'.format(cont_F_20))



        

