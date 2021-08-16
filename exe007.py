# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:40:05 2021

@author: Inayara
"""

'''desenvolva um programa que leia as duas notas de um aluno, calcule
 e mostre a sua média'''
 
nome=input('Aluno: ')
n1=float(input('Nota prova 1: '))
n2=float(input('Nota prova 2: '))
media1=(n1+n2)/2

nome2=input('Aluno: ')
n1=float(input('Nota prova 1: '))
n2=float(input('Nota prova 2: '))
media2=(n1+n2)/2
     
nome3=input('Aluno: ')
n1=float(input('Nota prova 1: '))
n2=float(input('Nota prova 2: '))
media3=(n1+n2)/2
médiasala = (media1+media2+media3)/3 


print("        ")
print(f'Aluno: {nome} \nNota prova 1: {n1} \nNota prova 2: {n2} \nMédia: {media1:.1f}') 

print(f'Aluno: {nome2} \nNota prova 1: {n1} \nNota prova 2: {n2} \nMédia: {media2:.1f}')    

print(f'Aluno:{nome3} \nNota prova 1: {n1} \nNota prova 2: {n2} \nMédia: {media3:.1f}') 

print(f'O aproveitamento geral da sala é {médiasala:.2f}')
