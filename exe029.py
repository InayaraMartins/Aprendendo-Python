# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:45:03 2021

@author: Inayara
"""

'''Exercício Python 29: Escreva um programa que leia a velocidade de
 um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
 ele foi  multado. A multa vai custar R$7,00 por cada Km acima 
 do limite.'''
 
 #COMO EU PENSEI
 
'''velocidade = float(input('Qual a velicidade atual do carro: '))
multa = (velocidade - 80)* 7
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança.')
else:
    print('MULTADO!Você excedeu o limite permitido que é de 80 km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança.')'''
    
#COMO O GUANABARA RESOLVEU    

velocidade = float(input('Qual a velicidade atual do carro: '))
multa = (velocidade - 80)* 7
if velocidade > 80:    
    print('MULTADO!Você excedeu o limite permitido que é de 80 km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')
    
 
 
 