'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o
 segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número 
 do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

altura_menor = altura_maior = numero_menor = numero_maior = None

for n in range(4):
    numero = input('Numero: ')
    altura = float(input('Altura: '))

    if altura_menor is None or altura < altura_menor:
        altura_menor = altura
        numero_menor = numero

    if altura_maior is None or altura > altura_maior:
        altura_maior = altura
        numero_maior = numero

print(f'O aluno mais alto e {numero_maior} com {altura_maior} cm')
print(f'O aluno mais baixo e {numero_menor} com {altura_menor} cm')