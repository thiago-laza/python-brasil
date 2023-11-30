'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é 
aquele que é divisível somente por ele mesmo e por 1.'''


numero = int(input('Digite um numero inteiro para saber se ele e ou nao primo: '))

cont = 1
divisores = 0

while cont <= numero:
    
    if numero % cont == 0:
        divisores += 1

    cont += 1

if divisores == 2:
    print(f'O numero {numero} e primo.')
else:
    print(f'O numero {numero} nao e um numero primo.')