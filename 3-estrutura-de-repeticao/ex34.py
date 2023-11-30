'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça 
um número inteiro e determine se ele é ou não 
um número primo.'''

numero = int(input('Informe um numero para verificar se ele e primo: '))


cont = 1
divisores = 0

while cont <= numero:
    if numero % cont == 0:
        divisores+=1

    cont+=1

if divisores == 2:
    print(f'O numero {numero} e primo.')
else:
    print(f'O numero {numero} nao e primo.')
