'''Faça um programa que leia 5 números e informe o maior número.'''

maior_numero = None

for i in range(1,6):
    numero = float(input(f'Digite o {i}⁰ numero: '))
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

print(maior_numero)
