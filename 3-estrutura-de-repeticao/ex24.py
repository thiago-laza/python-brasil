'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

numero_notas = int(input('Informe o numero de notas que serao digitadas: '))

cont = 0
acu = 0

while cont < numero_notas:
    notas = int(input(f'Digite a {cont+1}⁰ nota: '))
    acu+=notas
    cont+=1

media = acu/cont

print(f'A media das notas digitadas foi: {media}')