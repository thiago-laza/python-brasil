'''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.'''
def digitos_numero(n):
    n = str(num)
    return len(n)


num = int(input('Digite um numero: '))
print(f'O numero {num} possue {digitos_numero(num)} digitos.')