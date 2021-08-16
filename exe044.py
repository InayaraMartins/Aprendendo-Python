# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:36:45 2021

@author: Inayara
"""

'''Exercício Python 44: Elabore um programa que calcule o valor a 
ser pago por um produto, considerando o seu preço normal e 
condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format('LOJAS GUANABARA'))

preco = float(input('Qual o preço da compra: R$ ')) 
print('\nFORMAS DE PAGAMENTO\n')
print('[1] à vista dinheiro/cheque.')
print('[2] à vista no cartão.')
print('[3] em até 2x no cartão.')
print('[4] 3x ou mais no cartão.')

opcao = int(input('Qual a opção? '))

if opcao == 1:
    custo = preco - (preco*(10/100))
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, custo))
elif opcao == 2:
    custo = preco - (preco*(5/100))
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, custo))
elif opcao == 3:
    custo = preco/2
    print('Sua comprar será parcelada em 2 X de {} SEM JUROS.'.format(custo))
    print('Sua compra vai custar R${:.2f}'.format(preco))
elif opcao == 4: 
    parcela= int(input('Quantas parcelas: '))
    if parcela <3:
        print('Opção inválida. Tente outra vez!')
    else:
        custo = preco + (preco * (20/100))
        valorparcela = custo/ parcela
        print('Sua comprar será parcelada em {} X de {} COM JUROS.'.format(parcela,valorparcela))
        print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, custo))
    
else:
    print('Opção inválida! Tente outra vez!')