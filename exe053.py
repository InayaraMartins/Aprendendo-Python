# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 10:34:27 2021

@author: Inayara
"""

'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se
ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
    
    APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, 
    ANOTARAM A DATA DA MARATONA.'''
    
#len conta a quantidade de letra se for str, se for lista conta a qtd de elementos  

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #monta uma lista a partir dos espaços
junto = ''.join(palavras) # junta as palavras da lista sem o espaço
inverso=''
for i in range(len(junto)-1, -1,-1):
    inverso = inverso + junto[i] #esta concatenando str (juntando letra por letra)
print('Você digigitou a frase {} e o inverso é {}'.format(junto,inverso))
if junto == inverso:
    print('É um palíndromo') 
else:
    print('Não é um palíndromo')
