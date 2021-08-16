# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:39:41 2021

@author: Inayara
"""

'''Exercício Python 43: Desenvolva uma lógica que leia o peso e 
a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual o seu peso?(Kg) '))
altura = float(input('Qual sua altura?(m) '))
imc = peso/(altura**2)
pesoi = 21.75 *(altura**2)
print('O IMC dessa pessoa é de {:.1f}'. format(imc))

if imc < 18.5: 
    print('ABAIXO do Peso!')
    print('Seu peso ideal é {:.1f}'.format(pesoi))
  
elif imc < 25:
        print('Parabéns!!Você esta na faixa de peso IDEAL.')
        
else: 
    if imc < 30:
        print('Atenção!! Você esta com SOBREPESO!')
    elif imc < 40:
        print('Cuidado!!Você esta OBESO!')
    else:
        print('Consulte um médico! Você esta com Obesisade Morbida')
    print('Seu peso ideal é {:.1f}'.format(pesoi))

 
    

        
    
