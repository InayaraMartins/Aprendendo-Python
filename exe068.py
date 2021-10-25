# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:00:56 2021

@author: Inayara
"""

'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o 
computador. O jogo só será interrompido quando o jogador perder, mostrando o 
total de vitórias consecutivas que ele conquistou no final do jogo.'''


from random import randint

cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    escolha = input('Par ou ímpar? [P/I] ').upper()
    computador = randint(1,10)
    soma = jogador + computador
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}.Total de {soma} deu PAR')
        if escolha == 'P':
            print('Você venceu!!')
            cont = cont + 1                
        else:
            if escolha == 'I':
                print('Você perdeu!!')
                break
    elif soma % 2 == 1: 
        print(f'Você jogou {jogador} e o computador {computador}.Total de {soma} deu ÍMPAR')
        if escolha == 'I':
            print('Você venceu!!')
            cont = cont + 1  
        else:
            if escolha == 'P':
                print('Você perdeu!!')
                break
print('GAME OVER. Você conseguiu vencer {} vezes.'.format(cont))