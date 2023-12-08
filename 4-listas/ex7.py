'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''
vetor = []
soma=0
mult=1
for n in range(5):
    numero = int(input('Digite um numero: '))
    soma+=numero
    mult*=numero
    vetor.append(numero)
print(f'A soma dos valores digitados e: {soma}')
print(f'A multiplicacao dos valores digitados e: {mult}')
print(f'Os valores digitados sao: {vetor}')
