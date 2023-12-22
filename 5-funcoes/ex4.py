'''Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
se seu argumento for zero ou negativo.'''

def sinal(n):
    if n > 0:
        print(f'O numero {n} e positivo: P!')
    elif n == 0:
        print(f'O numero {n} e neutro: Nt!')
    else:
        print(f'O numero {n} e negativo: N!')


num = int(input('Digite um numero: '))
sinal(num)