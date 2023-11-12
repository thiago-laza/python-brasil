'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))
num_3 = float(input('Digite o terceiro numero: '))

if num_1 > num_2 and num_2 > num_3:
    print(f'Numeros digitados: {num_1}, {num_2} e {num_3}. Ordem decrescente: {num_1}, {num_2} e {num_3}.')
elif num_1 > num_3 and num_3 > num_2:
    print(f'Numeros digitados: {num_1}, {num_2} e {num_3}. Ordem decrescente: {num_1}, {num_3} e {num_2}.')
elif num_2 > num_1 and num_1 > num_3:
    print(f'Numeros digitados: {num_1}, {num_2} e {num_3}. Ordem decrescente: {num_2}, {num_1} e {num_3}.')
elif num_2 > num_3 and num_3 > num_1:
    print(f'Numeros digitados: {num_1}, {num_2} e {num_3}. Ordem decrescente: {num_2}, {num_3} e {num_1}.')
elif num_3 > num_1 and num_1 > num_2:
    print(f'Numeros digitados: {num_1}, {num_2} e {num_3}. Ordem decrescente: {num_3}, {num_1} e {num_2}.')
elif num_3 > num_2 and num_2 > num_1:
    print(f'Numeros digitados: {num_1}, {num_2} e {num_3}. Ordem decrescente: {num_3}, {num_2} e {num_1}.')