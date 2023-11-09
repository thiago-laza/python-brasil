'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

num1 = int(input('Informe um numero inteiro: '))
num2 = int(input('Informe outro numero inteiro: '))
num3 = float(input('Informe um numero real: '))

cal1 = (2*num1) * (num2/2)
cal2 = (3*num1) + num3
cal3 = num3**3

print(f'O produto do dobro do primeiro com metade do segundo e igual a: {cal1}')
print(f'A soma do triplo do primeiro com o terceiro e igual a: {cal2}')
print(f'O terceiro elevado ao cubo e igual a: {cal3}')