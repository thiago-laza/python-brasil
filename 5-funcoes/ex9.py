'''Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721.'''

def reverso(n):
    n = str(num)
    return n[::-1]


num = int(input('Digite um numero: '))
print(f'O inverso do numero {num} e {reverso(num)}')