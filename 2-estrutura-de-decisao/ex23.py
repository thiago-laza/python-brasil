'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
 Dica: utilize uma função de arredondamento.'''

num = float(input('Digite um numero para verificar se ele e inteiro ou decimal: '))

if num // 1 == num:
    print(f'{num} e um numero inteiro.')
else:
    print(f'{num} e um numero decimal.')