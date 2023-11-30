'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade 
de números impares.'''

cont_par = 0
cont_impar = 0

for i in range(1,11):
    numero = float(input(f'Digite o {i}⁰ numero: '))
    if numero % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f'Dos {i} numeros digitados, temos {cont_par} pares e {cont_impar} impares.')