# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:42:53 2021

@author: Inayara
"""

""" Exercício Python 34: Escreva um programa que pergunte o salário 
de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. 
 Para os inferiores ou iguais, o aumento é de 15%."""
 
salario = float(input('Qual é o salário do funcionário: '))

if salario <= 1250:
    novo = salario +(salario*0.15)
else:
    novo = salario +(salario*0.10)

print('Quem ganha R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))

 