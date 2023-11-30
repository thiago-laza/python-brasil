'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

numero = int(input('Digite um numero inteiro nao negativo para obter o seu fatorial: '))

while numero < 0:
    numero = int(input('Valor invalido. Digite um numero inteiro nao negativo para obter o seu fatorial: '))


produto = 1
while numero > 0:
    produto *= numero
    numero -= 1
    if produto == numero - 1:
        break
    

print(produto)
    