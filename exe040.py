# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 18:53:17 2021

@author: Inayara
"""

'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''


nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

média = (nota1 + nota2)/2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1,nota2,média))

if média < 5:
    print('Aluno Reprovado!')
elif média >= 7:
    print('Aluno Aprovado!')
else:
    print('Aluno está em Recuperação!')
    
