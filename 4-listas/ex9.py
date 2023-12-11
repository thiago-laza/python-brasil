'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos 
quadrados dos elementos do vetor.'''

vetor = []
soma = 0
produto = 0

for v in range(10):
    valor = int(input(f'Digite o valor {v}: '))
    vetor.append(valor)

for s in vetor:
    soma+=s

for p in vetor:
    produto+=p**2

print(f'Os valores informados sao: {vetor}')
print(f'A soma dos valores informados e: {soma}')
print(f'O produto dos valores informados e: {produto}')



