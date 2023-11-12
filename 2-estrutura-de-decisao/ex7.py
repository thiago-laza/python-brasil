'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))
num_3 = float(input('Digite o terceiro numero: '))

if num_1 > num_2 and num_2 > num_3:
    print(f'Dos numeros digitados: {num_1}, {num_2} e {num_3}, o maior e {num_1} e o menor e {num_3}')
elif num_1 > num_3 and num_3 > num_2:
    print(f'Dos numeros digitados: {num_1}, {num_2} e {num_3}, o maior e {num_1} e o menor e {num_2}')
elif num_2 > num_1 and num_1 > num_3:
    print(f'Dos numeros digitados: {num_1}, {num_2} e {num_3}, o maior e {num_2} e o menor e {num_3}')
elif num_2 > num_3 and num_3 > num_1:
    print(f'Dos numeros digitados: {num_1}, {num_2} e {num_3}, o maior e {num_2} e o menor e {num_1}')
elif num_3 > num_1 and num_1 > num_2:
    print(f'Dos numeros digitados: {num_1}, {num_2} e {num_3}, o maior e {num_3} e o menor e {num_2}')
elif num_3 > num_2 and num_2 > num_1:
    print(f'Dos numeros digitados: {num_1}, {num_2} e {num_3}, o maior e {num_3} e o menor e {num_1}')