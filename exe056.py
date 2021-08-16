# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 18:11:23 2021

@author: Inayara
"""

'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo 
de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é 
o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

qtdmulher = 0
nomehomem =''
maisvelho = 0
somaI = 0
for d in range(1,5):
    print(f'-'*5,'{}° pessoa'.format(d), '-'*5)
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    
    #média da idade
    somaI = somaI + idade
    
    if sexo == 'M':
        if idade > maisvelho:
            maisvelho = idade
            nomehomem = nome
    
    if sexo == 'F' and idade < 20:
        qtdmulher = qtdmulher + 1
    

print('A média de idade é {}.'.format(somaI/4))
print('O homem mais velho tem {} e se chama {}.'.format(maisvelho,nomehomem))
print('Ao todo são {} mulheres com idade menor que 20 anos.'.format(qtdmulher))
    


