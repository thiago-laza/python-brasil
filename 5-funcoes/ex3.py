'''Faça um programa, com uma função que necessite de três argumentos, e
 que forneça a soma desses três argumentos.'''

def soma(a,b,c):
    return a+b+c


a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))
print(f'A soma de {a}, {b} e {c} e igual a {soma(a,b,c)}')