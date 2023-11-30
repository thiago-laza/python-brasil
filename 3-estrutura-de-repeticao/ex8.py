'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

acumulador = 0

for i in range(1,6):
    numero = float(input(f'Digite o {i}⁰ numero: '))
    acumulador += numero

media = acumulador / i

print(f'A soma dos {i} numeros e igual a {acumulador} e a media e igual a {media}')