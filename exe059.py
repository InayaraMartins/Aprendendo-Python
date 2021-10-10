# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:23:21 2021

@author: Inayara
"""

'''Exercício Python 059: Crie um programa que leia dois valores e mostre 
um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:    
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>>>Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'. format(n1, n2, soma))
    
    elif opcao == 2:
        multicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}'. format(n1, n2, multicacao))
    
    elif opcao == 3:
        if n1 > n2:
            print('O maior é {}'. format(n1))
        else:
            print('O maior é {}'. format(n2))
    
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    
    else:
        print('Opção inválida. Tente novamente.') 

print('Finalizando...')
            
           



    