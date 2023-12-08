'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os 
números IMPARES no vetor impar. Imprima os três vetores.'''

numeros = []
par = []
impar = []

for n in range(20):
    valor = int(input('Digite um numero: '))
    numeros.append(valor)
    if numeros[n] % 2 == 0:
        par.append(numeros[n])
    else:
        impar.append(numeros[n])

print(f'Os valores digitados foram: {numeros}')
print(f'Os valores pares sao: {par}')
print(f'Os valores impares sao {impar}')

