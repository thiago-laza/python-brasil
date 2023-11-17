'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
Dica: utilize o operador módulo 
(resto da divisão).'''

num = int(input('Digite um numero para verificar se ele e ou nao par: '))

if num % 2 == 0:
    print(f'O numero {num} e par.')
else:
    print(f'O numero {num} nao e par.')